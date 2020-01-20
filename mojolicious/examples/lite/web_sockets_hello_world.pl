# Source: http://mojolicious.org/perldoc/Mojolicious/Guides/Tutorial#WebSockets
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
    <script>
      var ws = new WebSocket('<%= url_for('echo')->to_abs %>');
      ws.onmessage = function (event) {
        document.body.innerHTML += JSON.parse(event.data).msg;
      };
      ws.onopen = function (event) {
        ws.send(JSON.stringify({msg: 'I ♥ Mojolicious!'}));
      };
    </script>
  </head>
</html>
