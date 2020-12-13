package App;
use Dancer2;

set session => 'YAML';
debug "start";

get '/' => sub {
    my $counter = session('counter');
    debug $counter;
    $counter++;
    session counter => $counter;
    return $counter;
};

App->to_app;
