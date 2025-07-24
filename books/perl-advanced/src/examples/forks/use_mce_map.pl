use strict;
use warnings;

use MCE::Map;

main();

sub main {
    print "main PID: $$\n";
    my @results = mce_map { work($_) } 1..10;
    print "Results: @results\n";
}

sub work {
    my ($param) = @_;
    print "Param $param PID: $$\n";
    return $param * $param;
}
