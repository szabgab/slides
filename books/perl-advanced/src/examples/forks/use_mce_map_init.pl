use strict;
use warnings;

use MCE::Map;

main();

sub main {
    MCE::Map->init(
        max_workers => 3, # defaults to 4
        chunk_size => 2, # defaults to 1
    );
    print "main PID: $$\n";
    my @results = mce_map { work($_) } 1..10;
    print "Results: @results\n";
}

sub work {
    my ($param) = @_;
    print "Param $param PID: $$\n";
    #exit 23 if $param == 2;
    return $param * $param;
}
