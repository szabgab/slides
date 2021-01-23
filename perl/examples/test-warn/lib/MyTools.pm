package MyTools;
use strict;
use warnings;
use DateTime;

our $VERSION = '0.01';

use Exporter qw(import);
our @EXPORT_OK = qw(fibo);

sub fibo {
    my ($n) = @_;

    die "Need to get a number\n" if not defined $n;
    if ($n <= 0) {
        warn "Given number must be > 0";
        return;
    }
    #warn "Some other warning @_";
    return 1 if $n == 1 or $n == 2;

    my @fib = (1, 1);
    for (3..$n) {
        push @fib, $fib[-1]+$fib[-2];
    }
    return $fib[-1];
}

1;

