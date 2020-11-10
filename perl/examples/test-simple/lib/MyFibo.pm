package MyFibo;
use strict;
use warnings;

use Exporter qw(import);
our @EXPORT_OK = qw(fibo);

sub fibo {
    my ($n) = @_;
    return $n if $n == 0 or $n == 1;

    my @fib = (0, 1);
    for (2..$n) {
        push @fib, $fib[-1] + shift @fib;
    }
    return $fib[-1];
}


1;

