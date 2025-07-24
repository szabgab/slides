package Compute;
use strict;
use warnings;

#use base 'Exporter';
#our @EXPORT_OK = qw(add);

use Exporter qw(import);
our @EXPORT_OK = qw(add);

sub add {
    my ($x, $y) = @_;
    return $x+$y;
}

1;

