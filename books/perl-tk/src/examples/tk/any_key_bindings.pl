use strict;
use warnings;
use 5.010;

use Tk;

my $top = MainWindow->new;

my $label = $top->Label(
    -text => 'Press any key',
    -font => ['fixed', 40],
    -background => 'yellow',
);
$label->pack();

sub key_pressed {
    my $window = shift;
    my $event = $window->XEvent;
    #say $event;
    say $event->K;
}

$top->bind("<Any-KeyPress>", \&key_pressed);


MainLoop;
