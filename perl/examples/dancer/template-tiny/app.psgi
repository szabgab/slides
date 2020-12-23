package App;
use Dancer2;

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
    };
};

App->to_app;
