use strict;
use warnings;

use FindBin qw($Bin);
use lib "$Bin/../lib";
use MySimpleCalc qw(sum);

print sum(1, 1),    "  2\n";
print sum(2, 2),    "  4\n";
print sum(2, 2, 2), "  6\n";

