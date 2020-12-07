package App;
use Dancer2;

set show_errors => $ENV{DANCER_ERROR};

get '/' => sub {
    return 'Hello World! <a href="/calc">calc</a>';

};

get '/calc' => sub {
    my $x = 1;
    my $y = 0;
    my $z = $x / $y;
    return 'OK';
};

App->to_app;
