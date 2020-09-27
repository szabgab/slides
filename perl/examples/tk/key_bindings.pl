use strict;
use warnings;
use 5.010;

use Tk;

my $top = MainWindow->new;

$top->bind("<a>", sub { say 'a pressed' });
$top->bind("<A>", sub { say 'A pressed (shift-a)' });
$top->bind("<Control-a>", sub { say 'Ctrl-a pressed' });
$top->bind("<Alt-a>", sub { say 'Alt-a pressed' });
$top->bind("<F1>", sub { say 'F1' });

MainLoop;
