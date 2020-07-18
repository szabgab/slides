package App;
use Dancer2;

get '/' => sub {
    return 'Hello World!';
};

App->to_app;
