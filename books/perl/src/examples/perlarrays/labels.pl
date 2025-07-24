use strict;
use warnings;


OUTER:
while (1) {
    print "start outer\n";
    while (1) {
        print "start inner\n";
        last OUTER;
        print "end inner\n";
    }
    print "end outer\n";
}
print "done\n";
