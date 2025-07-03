use strict;
use warnings;

use FindBin;
use lib "$FindBin::Bin/../lib";
use MySimpleCalc qw(sum);

if (sum(1, 1) == 2) {
    print "ok\n";
} else {
    print "not ok\n";
}

if (sum(2, 2) == 4) {
    print "ok\n";
} else {
    print "not ok\n";
}

if (sum(2, 2, 2) == 6) {
    print "ok\n";
} else {
    print "not ok\n";
}



