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

get '/user/:id' => sub {
    my $id = route_parameters->get('id');
    if (not valid_id($id)) {
        status 'not_found';
        return 'No such ID';
    }
    return $id;
};

App->to_app;

sub valid_id {
    my ($id) = @_;

    # Database lookup
    return if $id <= 0;
    return if $id >= 42;
    return 1;
}
