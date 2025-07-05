use Mojolicious::Lite;

get '/' => { text => 'Hello World' };

get '/echo' => sub {
    my $c = shift;
    $c->render('echo');
};

post '/echo' => sub {
    my $c = shift;
    $c->render( 'response', msg => $c->param('q') );
};
 
app->secrets(['My very secret passphrase.']);

app->start;

__DATA__
     
@@ echo.html.ep
     
What are you looking for?
<form method="POST"><input name="q"><input type="submit" value="Echo"></form>

@@ response.html.ep
     
You typed: <%= $msg %>

