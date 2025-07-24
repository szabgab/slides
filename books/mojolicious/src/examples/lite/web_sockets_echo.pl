use Mojolicious::Lite;

websocket '/echo' => sub {
  my $c = shift;
  $c->on(json => sub {
    my ($c, $hash) = @_;
    $hash->{msg} = "echo: $hash->{msg}";
    $c->send({json => $hash});
  });
};

get '/' => 'index';

app->start;
__DATA__

@@ index.html.ep
<!DOCTYPE html>
<html>
  <head>
    <title>Echo</title>
    <input type="text" id="msg">
    <div id="output">
    </div>
    <script>
      var ws = new WebSocket('<%= url_for('echo')->to_abs %>');
      ws.onmessage = function (event) {
          var msg = JSON.parse(event.data).msg;
          console.log('Received', msg);
          document.getElementById('output').innerHTML += msg + '<br>';
      };
      //ws.onopen = function (event) {
      //};

      function send(e) {
          if (e.keyCode !== 13) {
              return false;
          }
          var msg = document.getElementById('msg').value;
          document.getElementById('msg').value = '';
          console.log('send', msg);
          ws.send(JSON.stringify({msg: msg}));
      }

      document.getElementById('msg').addEventListener('keypress', send);
      document.getElementById('msg').focus();
    </script>
  </head>
</html>

