use strict;
use warnings;

use List::UtilsBy qw(sort_by);

my @numbers = (2, -3, 4);
my @sorted = sort @numbers;
print "@sorted\n";

@sorted = sort { abs($a) <=> abs($b) } @numbers;
print "@sorted\n";

@sorted = sort_by { abs($_) }  @numbers;
print "@sorted\n";



