use strict;
use warnings;
use 5.010;

use Tk;

my $top = MainWindow->new;

$top->bind("<Any-KeyPress>", sub { say 'any key' });


MainLoop;
