package App;
use Dancer2;

my $counter = 0;

get '/' => sub {
    $counter++;
    return $counter;
};

App->to_app;
