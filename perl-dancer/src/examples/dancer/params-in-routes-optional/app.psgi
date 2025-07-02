package App;
use Dancer2;

get '/' => sub {
    return q{
        <a href="/user/foobar">/user/foobar</a><br>
        <a href="/user/">/user/</a><br>
        <a href="/user">/user</a><br>
    };
};

get '/user/:username?' => sub {
    my $username = route_parameters->get('username');
    return 'undef' if not defined $username;
    return 'empty' if $username eq '';
    return $username;
};

App->to_app;
