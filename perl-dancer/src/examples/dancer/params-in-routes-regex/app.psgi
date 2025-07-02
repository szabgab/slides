package App;
use Dancer2;

get '/' => sub {
    return q{
        <a href="/user/foobar-42">foobar</a><br>
    };
};

get '/user/:username[StrMatch[qr{^[a-z]+-[0-9]+$}]]' => sub {
    my $username = route_parameters->get('username');
    return $username;
};

App->to_app;
