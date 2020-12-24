package App;
use Dancer2;

debug config->{template};

get '/' => sub {
    return template 'main.tt', {
        name => 'Perl Dancer',
        on => 0,
        languages => ['Perl', 'Python', 'Go'],
        perl => {
            creator => 'Larry Wall',
            release => 1987,
        },
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
        template_name => config->{template},
    };
};

App->to_app;
