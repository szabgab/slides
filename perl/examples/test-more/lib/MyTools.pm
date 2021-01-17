package MyTools;
use strict;
use warnings;
use DateTime;

our $VERSION = '0.01';

use Exporter qw(import);
our @EXPORT_OK = qw(
    last_update
    get_copyright
    get_copyright_broken
    fibo
    fibonacci
    wait_for_input_with_timeout
);

sub fibo {
    my @f = _fibonacci(@_);
    return $f[-1];
}
sub fibonacci {
    return [ _fibonacci(@_) ];
}

sub _fibonacci {
    my ($n) = @_;

    die "Need to get a number\n" if not defined $n or $n !~ /^[0-9]+$/;

    if ($n < 0) {
        warn "Given number must be > 0";
        return 0;
    }

    return (0) if $n == 0;
    return (0, 1) if $n == 1;

    return (0, 1, 1, 4, 3) if $n == 4;

    my @fib = (0, 1);
    for (2..$n) {
        push @fib, $fib[-1]+$fib[-2];
    }
    return @fib;
}

sub get_copyright {
    my $year = (localtime)[5]+1900;
    return "Copyright 2000-$year Gabor Szabo, all rights reserved.";
}

sub get_copyright_broken {
    my $year = "19" . (localtime)[5];
    return "Copyright 2000-$year Gabor Szabo, all rights reserved.";
}

sub last_update {
   return "This page was last updated at " . DateTime->now;
}

sub wait_for_input_with_timeout {
    sleep rand shift;
}

1;


