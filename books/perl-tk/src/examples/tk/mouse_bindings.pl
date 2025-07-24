use strict;
use warnings;
use 5.010;

use Tk;

my $top = MainWindow->new;

my $label = $top->Label(
    -text => "Click on the buttons of the mouse\nand look at the terminal.",
    -font => ['fixed', 40],
    -background => 'purple',
);
$label->pack;


$top->bind('<ButtonPress-1>', sub { say 'ButtonPress-1' }); # Mouse left button click
$top->bind('<ButtonPress-2>', sub { say 'ButtonPress-2' }); # Mouse middle button click
$top->bind('<ButtonPress-3>', sub { say 'ButtonPress-3' }); # Mouse right button click

$top->bind('<ButtonRelease-1>', sub { say 'ButtonRelease-1' }); # Mouse left button release
$top->bind('<ButtonRelease-2>', sub { say 'ButtonRelease-2' }); # Mouse middle button release
$top->bind('<ButtonRelease-3>', sub { say 'ButtonRelease-3' }); # Mouse right button release

$top->bind('<B1-Motion>',sub { say 'Motion-1' } ); # Moving mouse while left button is pressed
$top->bind('<B2-Motion>',sub { say 'Motion-2' } ); # - middle button -
$top->bind('<B3-Motion>',sub { say 'Motion-3' } ); # - right button -

MainLoop;
