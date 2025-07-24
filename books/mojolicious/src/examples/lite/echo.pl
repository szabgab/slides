use Mojolicious::Lite;



get '/' => { text => 'Hello World' };

get '/echo' => { text => q{
    <form method="POST">
    <input name="q">
    <input type="submit" value="Echo">
    </form>
}};

post '/echo' => sub {
    my $c = shift;
    $c->render( text => $c->param('q') );
};
 
app->secrets(['My very secret passphrase.']);

app->start;

