package App;
use Dancer2;
use Data::Dumper qw(Dumper);

get '/' => sub {
    return q{
        <a href="/user/foobar">/user/foobar</a><br>
        <a href="/user/foo/bar">/user/foo/bar</a><br>
    };
};

get '/user/**' => sub {
    my ($parts) = splat;
    return Dumper $parts;
};

App->to_app;
