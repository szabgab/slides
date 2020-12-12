package App;
use Dancer2;

set 'template'     => 'template_toolkit';

get '/' => sub {
    return template 'main.tt', {
        name => 'Perl Dancer',
        on => 0,
        languages => ['Perl', 'Python', 'Go'],
        fruits => [
            {
                name => 'Apple',
                color => 'Red',
            },
            {
                name => 'Banana',
                color => 'Yellow',
            },
            {
                name => 'Peach',
                color => 'Peach',
            }
        ],
    };
};

App->to_app;
