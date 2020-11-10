package MySimpleCalcFixed;
use strict;
use warnings;

use Exporter qw(import);
our @EXPORT_OK = qw(sum);

sub sum {
    my $sum = 0;
    $sum += $_ for @_;
    return $sum;
}

1;

