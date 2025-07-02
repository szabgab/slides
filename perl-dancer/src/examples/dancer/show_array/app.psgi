package App;
use Dancer2;

set 'template'     => 'template_toolkit';

get '/' => sub {
    my @planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn');
    return template 'page', { planets => \@planets };
};

App->to_app;
