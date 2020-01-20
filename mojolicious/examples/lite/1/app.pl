use Mojolicious::Lite;

get '/' => sub {
    my $c = shift;
    $c->render('index');
};

get '/echo' => sub {
    my $c = shift;
    $c->render('echo', msg => undef);
};

post '/echo' => sub {
    my $c = shift;
    $c->render( 'echo', msg => $c->param('q') );
};
 
app->secrets(['My very secret passphrase.']);

app->start;

__DATA__


@@ layouts/wrapper.html.ep
<!DOCTYPE html>
<html>
<head>
  <title></title>
  <link href="/style.css" rel="stylesheet">
</head>

<body>
<div id="menu">
<ul>
  <li><a href="/">home</a></li>
  <li><a href="/echo">echo</a></li>
</ul>
</div>

<%= content %>

</body>
</html>

     
@@ echo.html.ep
% layout 'wrapper';
     
What are you looking for?
<form method="POST"><input name="q"><input type="submit" value="Echo"></form>

% if (defined $msg) {
    You typed: <%= $msg %>
% }

@@ index.html.ep
% layout 'wrapper';

Hello World<br>
Try <a href="/echo">Echo</a>
