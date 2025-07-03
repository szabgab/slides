use strict;
use warnings;

use FindBin qw($Bin);
use lib "$Bin/../lib";
use MySimpleCalc qw(sum);

print sum(1, 1), "  2\n";
print sum(2, 2), "  4\n";
print sum(2, 2, 2), "  6\n";
print sum(3, 3), "  6\n";
print sum(4, 4), "  8\n";
print sum(5, 5), "  10\n";
print sum(6, 6), "  12\n";
print sum(7, 7), "  14\n";

