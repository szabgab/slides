use strict;
use warnings;

main();

sub main {
    my $parent = getppid();
    print "PID: $$ from parnet: $parent\n";;
}

