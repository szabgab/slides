use strict;
use warnings;

use List::UtilsBy qw(sort_by);

sub func {
    my ($val) = @_;
    print "func $val\n";
    return $val;
}

my @sorted = sort { func($a) <=> func($b) } (4, 3, 2, 1);
print "@sorted\n";
print "\n";  # looks like func is called n * log(n)

@sorted = sort_by { func($_) } (4, 3, 2, 1);
print "@sorted\n";
print "\n";  # func is only called n times

