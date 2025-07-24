package MyTools;
use strict;
use warnings;
use Scalar::Util qw(looks_like_number);

our $VERSION = '0.01';

use Exporter qw(import);
our @EXPORT_OK = qw(fibo add);

sub fibo {
    my ($n) = @_;

    die "Need to get a parameter\n" if not defined $n;
    die "Need to get a number\n" if not looks_like_number($n);
    if ($n <= 0) {
        warn "Given number must be > 0";
        return;
    }
    return 1 if $n == 1 or $n == 2;
    #warn "Some other warning @_";

    my @fib = (1, 1);
    for (3..$n) {
        push @fib, $fib[-1]+$fib[-2];
    }
    return $fib[-1];
}

sub add {
    my ($x, $y) = @_;
    return $x + $y;
}

1;

