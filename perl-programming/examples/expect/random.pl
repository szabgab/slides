use strict;
use warnings;

my $x = rand();
if ($x < 0.3) {
    print "abc\n";
} elsif ($x < 0.6) {
    print "def\n";
} else {
    print "xyz\n";
}
