use Mojolicious::Lite;

get '/' => { text => q{
<ul>
    <li><a href="/list/home">/list/home</a></li>
    <li><a href="/user?id=19">/user?id=19</a></li>
    <li><a href="/item/42">/item/42</a></li>
    <li><a href="/phone/1.234.567890">/phone/1.234.567890</a></li>
    <li><a href="/path/one/two/three">/path/one/two/three</a></li>
</ul>
}};

get '/list/home' => { text => q{
    Found /list/home
}};

get '/user' => sub {
    my $c = shift;
    $c->render( text => "user ID " . $c->param('id') );
};

get '/item/:id' => sub {
    my $c = shift;
    $c->render( text => "item ID " . $c->param('id') );
};

get '/phone/#number' => sub {
    my $c = shift;
    $c->render( text => "phone number: " . $c->param('number') );
};
   
get '/path/*anything' => sub {
    my $c = shift;
    $c->render( text => "path: " . $c->param('anything') );
};

app->secrets(['My very secret passphrase.']);

app->start;


