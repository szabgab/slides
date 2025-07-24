package MyApp;
use strict;
use warnings;

use Exporter qw(import);
our @EXPORT_OK = qw(add div);


sub add {
    my ($x, $y) = @_;
    return $x + $y;
}

sub div {
    my ($x, $y) = @_;
    return $x / $y;
}

1;


