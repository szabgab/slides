package App;
use Dancer2;

#set session => 'YAML';

get '/' => sub {
    my $counter = session('counter');
    $counter++;
    session counter => $counter;
    return $counter;
};

App->to_app;
