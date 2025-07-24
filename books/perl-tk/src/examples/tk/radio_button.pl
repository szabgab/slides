use strict;
use warnings;
use 5.010;

use Tk;

my $top = MainWindow->new;

my @planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn');
my $the_planet;
for my $planet (@planets) {
    my $rb = $top->Radiobutton(
        -text     => $planet,
        -variable => \$the_planet,
        -value    => $planet,
        -font     => ['fixed', 15]
    );
    $rb->pack(-side => 'left');
}

my $btn = $top->Button(
    -text    => 'Click me',
    -font    => ['fixed', 20],
    -command => \&do_on_click,
);
$btn->pack();
MainLoop;

sub do_on_click {
    say $the_planet;
    say '----';
}

