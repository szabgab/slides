#!/usr/bin/perl
use strict;
use warnings;

use Log::Dispatch;
use Log::Dispatch::Screen;

my $logger = Log::Dispatch->new;
$logger->add( Log::Dispatch::Screen->new(
    name => 'screen',
    #min_level => 'warning',
    min_level => 'debug',
));

fib(4);
fib(0);

sub fib {
    my $n = shift;
    $logger->debug("fib($n)");

    if ($n < 1) {
        $logger->error("fib($n) is invalid");
        return;
    }

    if ($n == 1 or $n == 2) {
        return 1;
    }
    return fib($n-1) + fib($n-2);
}
