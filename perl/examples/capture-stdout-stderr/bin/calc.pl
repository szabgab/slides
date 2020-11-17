use strict;
use warnings;

use CalcOutput qw(calc_and_print);

die "Usage: $0 NUM NUM\n" if @ARGV != 2;

my $result = calc_and_print(@ARGV);
print "The result is $result.\n";
