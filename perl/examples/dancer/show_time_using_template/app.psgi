package App;
use Dancer2;
use DateTime;

get '/' => sub {
    my $dt = DateTime->now;
    return template 'page', {
        timestamp => $dt->strftime( '%Y-%m-%d %H:%M:%S' ),
    };
};

App->to_app;
