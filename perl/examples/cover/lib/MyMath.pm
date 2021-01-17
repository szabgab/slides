package MyMath;
use strict;
use warnings;

use Exporter qw(import);
our @EXPORT_OK = qw(add div fibo);

our $VERSION = '0.02';

=head1 NAME

MyMath - some tools to show test coverage

=head1 SYNOPSIS

Short example

=cut

sub add {
	return $_[0] + $_[1];
}

sub div {
	return $_[0] / $_[1];
}


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

