package App;
use Dancer2;

get '/' => sub {
    return 'Hello World!';
};

get '/calc' => sub {
    my $x = 1;
    my $y = 0;
    my $z = $x / $y;
    return 'OK';
};

App->to_app;
