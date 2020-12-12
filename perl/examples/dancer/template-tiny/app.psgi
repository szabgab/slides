package App;
use Dancer2;

# The default templating engine is the Tiny engine https://metacpan.org/pod/Dancer2::Template::Tiny
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
