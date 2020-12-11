package App;
use Dancer2;

set log => 'warning';

get '/' => sub {
    debug 'debug in main';
    info 'info in main';
    warning 'warning in main';
    error 'error in main';

    return 'Hello World!';
};

App->to_app;
