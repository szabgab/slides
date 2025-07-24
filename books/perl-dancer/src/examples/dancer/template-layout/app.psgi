package App;
use Dancer2;


get '/' => sub {
    return template 'main.tt', {
        title => 'Perl Dancer',
    };
};

App->to_app;
