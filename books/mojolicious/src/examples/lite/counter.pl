use Mojolicious::Lite;

my $counter = 0;

get '/' => sub {
    my $c = shift;
    $counter++;
    $c->stash( counter => $counter );
    $c->render( 'counter' )
};

app->start;

__DATA__
@@ counter.html.ep
% layout 'wrapper';
Counter: <%= $counter %>


@@ layouts/wrapper.html.ep
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport"
     content="width=device-width, initial-scale=1, user-scalable=yes">
  <title></title>
</head>
<body>

<%= content %>

</body>
</html>

