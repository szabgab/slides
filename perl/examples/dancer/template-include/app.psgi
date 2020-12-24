package App;
use Dancer2;

get '/' => sub {
    return template 'main.tt', {
        name => 'Perl Dancer',
    };
};

App->to_app;
