package App;
use Dancer2;

get '/' => sub {
    my $config = config();
    return '<pre>' . to_json($config, {pretty => 1, canonical => 1}) . '</pre>';
};

App->to_app;
