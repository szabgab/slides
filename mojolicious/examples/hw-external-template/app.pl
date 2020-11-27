use Mojolicious::Lite  -signatures;

get '/' => sub ($c) {
  $c->render(template => 'index');
};

app->start;

