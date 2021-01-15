use strict;
use warnings;

use Range::Iter qw(range_iter);

my $iter = range_iter(1, 10, 2);
while (my $val = $iter->()) {
    print "$val\n"; # 1, 3, 5, 7, 9
}
