package MyTools2;
use strict;
use warnings;

our $VERSION = '0.01';

use base 'Exporter';
our @EXPORT = qw(sum fibonacci multiply get_copyright);

sub sum {
    my $sum = 0;
    $sum += $_ for @_;
    return $sum;
}

1;


