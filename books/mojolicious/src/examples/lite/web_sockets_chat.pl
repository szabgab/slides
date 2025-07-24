use Mojolicious::Lite;
use DateTime;
use Data::Dumper qw(Dumper);
# Chrome seems to reach timeout after 15 sec
# Firefox seems to reach timeout after 35-40 sec
# When I enabled the heartbeat from JavaScript the timeout went down in FF to 15 sec


my %clients;

websocket '/chat' => sub {
    my $c = shift;
    my $tx_id = sprintf "%s", $c->tx;
    $clients{$tx_id} = { ws => $c->tx };

    $c->on(json => sub {
        my ($ws, $hash) = @_;
        $c->app->log->debug("From $ws received " . Dumper $hash);

        if ($hash->{heartbeat}) {
            $ws->send({json => {heartbeat => $hash->{heartbeat}}});
            return;
        }

        my $dt   = DateTime->now( time_zone => 'Asia/Tokyo');

        if ($hash->{login}) {
            $clients{$tx_id}{user_name} = $hash->{login};
            $ws->send({json => {login => 'ok'}});
            # TODO: notify everyone who joined the conversation
            foreach my $ws (keys %clients) {
                next if $ws eq $tx_id;
                $clients{$ws}{ws}->send({json => {
                    msg => $dt->hms . " $clients{$tx_id}{user_name} has joined the conversation"
                }});
            }

            return;
        }

        foreach my $ws (keys %clients) {
            my $msg = $dt->hms . ($ws eq $tx_id ? " $hash->{msg}" : " $clients{$tx_id}{user_name}: $hash->{msg}");
            $clients{$ws}{ws}->send({json => {
                msg => $msg,
            }});
        }

        return;
    });

    $c->on(finish => sub {
        my ($ws, $code, $reason) = @_;
        $c->app->log->debug( "Finished $ws Code $code reason: '" . ( $reason // '' ) .  "'");
        # code was 1006
        # reason was undef
        # TODO: notify everyone who left the conversation

        my $dt   = DateTime->now( time_zone => 'Asia/Tokyo');
        foreach my $ws (keys %clients) {
            next if $ws eq $tx_id;
            $clients{$ws}{ws}->send({json => {
                msg => $dt->hms . " $clients{$tx_id}{user_name} has left the conversation"
            }});
        }

        delete $clients{$ws};
        return;
    });
};

get '/' => 'index';

app->start;
__DATA__

@@ index.html.ep
<!DOCTYPE html>
<html>
  <head>
    <title>Chat</title>
    <script>
        var ws;
        var user_name;
        var heartbeat_interval = null;
        function login(e) {
            if (e.keyCode !== 13) {
                  return false;
            }
            user_name = document.getElementById('name').value;
            //console.log(user_name);
            document.getElementById('login_name').innerHTML = user_name;
            document.getElementById('login').style.display = 'none';
            document.getElementById('chat').style.display = 'block';

            setup();
        }

        function setup() {
            ws = new WebSocket('<%= url_for('chat')->to_abs %>');

            ws.onmessage = function (event) {
                var data = JSON.parse(event.data);
                if (! data.msg) {
                    return;
                }
                console.log('Received', data.msg);
                document.getElementById('output').innerHTML = data.msg + '<br>' + document.getElementById('output').innerHTML;
            };

            ws.onopen = function (event) {
                ws.send(JSON.stringify({login: user_name}));

                // heartbeat: not based on http://django-websocket-redis.readthedocs.io/en/latest/heartbeats.html
                if (heartbeat_interval === null) {
                    heartbeat_interval = setInterval(function() {
                        ws.send(JSON.stringify({heartbeat: user_name}));
                    }, 14000);
                }
            };

            ws.onclose = function(){
                if (heartbeat_interval !== null) {
                    clearInterval(heartbeat_interval);
                }
                setTimeout(setup, 1000);
            };
        };

        function send(e) {
            if (e.keyCode !== 13) {
                  return false;
            }
            var msg = document.getElementById('msg').value;
            document.getElementById('msg').value = '';
            console.log('send', msg);
            ws.send(JSON.stringify({msg: msg}));
        }
        
        function onload() {
            //console.log('onload');
            document.getElementById('name').addEventListener('keypress', login);
            document.getElementById('msg').addEventListener('keypress', send);
            document.getElementById('msg').focus();
        }
    </script>

    <style>
      #chat {
        display: none;
      }
    </style>
  </head>
  <body onload="onload()">
    <div id="login">Your name: <input type="text" id="name"></div>
    <div id="chat">
        Logged in as <span id="login_name"></span><br>
        <input type="text" id="msg" placeholder="Your message">
        <div id="output"></div>
    </div>
  </body>
</html>

