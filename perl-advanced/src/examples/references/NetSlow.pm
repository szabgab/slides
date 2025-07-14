package NetSlow;
use strict;
use warnings;

use base 'Exporter';
our @EXPORT_OK = qw(compute);

sub compute {
    my $sum = 0;
    $sum += $_ for @_;

    $sum += int (time / 60 + $sum);
    sleep(3);
    return $sum;
}

1;

