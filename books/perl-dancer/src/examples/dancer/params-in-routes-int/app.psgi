package App;
use Dancer2;

get '/' => sub {
    return q{
        <a href="/user/1">One</a><br>
        <a href="/user/2">Two</a><br>
        <a href="/user/foobar">foobar</a><br>
        <a href="/user">user</a><br>
        <a href="/user/">user/</a><br>
        <a href="/user/a/b">a/b</a><br>
        <a href="/user/-1">-1</a><br>
        <a href="/user/1.1">1.1</a><br>
    };
};

get '/user/:id[Int]' => sub {
    my $id = route_parameters->get('id');
    return $id;
};

App->to_app;
