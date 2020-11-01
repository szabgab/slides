package CalcOutput;
use strict;
use warnings;

use Exporter qw(import);
our @EXPORT_OK = qw(calc_and_print);

sub calc_and_print {
    my ($x, $y) = @_;

    my $z = $x + $y;
    print "The result on STDOUT is $z\n";
    print STDERR "Some messages sent to STDERR\n";

    return $z;
}


1;

