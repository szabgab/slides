use strict;
use warnings;

use Tk;

my $top = MainWindow->new;

my @planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn');
my %plnt;
for my $planet (@planets) {
    $plnt{$planet} = 0;
    my $cb = $top->Checkbutton(
        -text     => $planet,
        -variable => \$plnt{$planet},
        -font     => ['fixed', 15]
    );
    $cb->pack(-side => 'left');
}

my $btn = $top->Button(
    -text    => 'Click me',
    -font    => ['fixed', 20],
    -command => \&do_on_click,
);
$btn->pack();
MainLoop;

sub do_on_click {
    print("Clicked\n");
    for my $planet (sort keys %plnt) {
        printf("%-10s %s\n", $planet, $plnt{$planet});
    }
    print("----\n");
}



