use strict;
use warnings;

use FindBin;
use lib "$FindBin::Bin/../lib";
use MySimpleCalc qw(sum);

ok( sum(1, 1)    == 2 );
ok( sum(2, 2)    == 4 );
ok( sum(2, 2, 2) == 6 );

sub ok {
    my ($true) = @_;

    if ($true) {
        print "ok\n";
    } else {
        print "not ok\n";
    }
}
