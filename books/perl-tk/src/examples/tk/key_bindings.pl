use strict;
use warnings;
use 5.010;

use Tk;

my $top = MainWindow->new;

my $label = $top->Label(
    -text => 'Press a, A, Ctrl-A, Alt-a, F1 and observe on the console',
    -font => ['fixed', 40],
    -background => 'yellow',
);
$label->pack();

$top->bind("<a>", sub { say 'a pressed' });
$top->bind("<A>", sub { say 'A pressed (shift-a)' });
$top->bind("<Control-a>", sub { say 'Ctrl-a pressed' });
$top->bind("<Alt-a>", sub { say 'Alt-a pressed' });
$top->bind("<F1>", sub { say 'F1' });

MainLoop;
