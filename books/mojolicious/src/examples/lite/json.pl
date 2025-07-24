use Mojolicious::Lite;

get '/' => { text => q{
<ul>
    <li><a href="/list">/list</a></li>
</ul>
}};

get '/list' => sub {
    my $c = shift;
    my @people = (
        {
            name => 'Foo',
            id  => 19,
        },
        {
            name => 'Bar',
            id  =>  23,
        },
        {
            name => 'Qux',
            id  =>  42,
        },
    );

    $c->render( json => \@people );
};

app->secrets(['My very secret passphrase.']);

app->start;

