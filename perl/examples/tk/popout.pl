use strict;
use warnings;
use 5.010;

use Tk;

my $top = MainWindow->new;
my $btn = $top->Button(
    -text    => 'Click me',
    -font    => ['fixed', 20],
    -command => \&do_on_click,
);
$btn->pack;

my $pop;

MainLoop;


sub do_on_click {
    print("Clicked\n");
    if (not $pop) {
        say 'Creating';
        $pop = $top->Toplevel();
        $pop->Frame(-width => 150, -height => 230)->pack;
        $pop->protocol('WM_DELETE_WINDOW' => [\&picked, $pop, undef]);
        #$pop->overrideredirect(1);

        my @colors = qw(blue red yellow);
        for my $color (@colors) {
            my $btn = $pop->Button(
            -font    => ['fixed', 20],
            -command => [\&picked, $pop, $color],
            -width   => 20,
            -bg      => $color,
            );
            $btn->pack;
        }
    }
    $pop->Popup(-popanchor  => 'c', -overanchor => 'c', -popover => $top);
}
# TODO: modal (so I cannot click on the main window as long as this is here)

sub picked {
    my ($pop, $color) = @_;
    if ($color) {
        say $color;
        $btn->configure(-background => $color);
    }
    $pop->withdraw;
}
