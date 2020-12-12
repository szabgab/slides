package App;
use Dancer2;

set 'template'     => 'template_toolkit';

get '/' => sub {
    return template 'main.tt', {
        name => 'Perl Dancer',
    };
};

App->to_app;
