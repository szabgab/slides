package App;
use Dancer2;

set 'template'     => 'template_toolkit';
set 'layout'       => 'main.tt';

get '/' => sub {
    return template 'main.tt', {
        title => 'Perl Dancer',
    };
};

App->to_app;
