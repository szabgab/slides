use Mojolicious::Lite;

get '/' => { text => 'Hello World' };

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
     
@@ echo.html.ep
     
What are you looking for?
<form method="POST"><input name="q"><input type="submit" value="Echo"></form>

% if (defined $msg) {
    You typed: <%= $msg %>
% }

