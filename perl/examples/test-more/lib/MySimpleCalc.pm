package MySimpleCalc;
use strict;
use warnings;

use Exporter qw(import);
our @EXPORT_OK = qw(sum);

sub sum {
    return $_[0] + $_[1];
}

1;

