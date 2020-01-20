#!/usr/bin/perl
use strict;
use warnings;
use 5.010;

use Log::Dispatch;
use Log::Dispatch::Screen;
use Log::Dispatch::File;
use POSIX ();

my $logger = Log::Dispatch->new;
$logger->add( Log::Dispatch::Screen->new(
    name => 'screen',
    min_level => 'warning',
));
$logger->add( Log::Dispatch::File->new(
    name      => 'file',
    min_level => 'debug',
    filename  => POSIX::strftime("%Y-%m-%d", localtime) . '.log',
    callbacks => \&callback,
));

fib(4);
fib(0);

sub fib {
    my $n = shift;
    $logger->debug("fib($n)");

    if ($n < 1) {
        $logger->error("fib($n) is invalid");
        $logger->log(level => 'error', message => 'another');
        return;
    }

    if ($n == 1 or $n == 2) {
        return 1;
    }
    return fib($n-1) + fib($n-2);
}

sub callback {
    my %arg = @_;
    my ($package, $filename, $line) = caller(6);
    return "$arg{message}  in $filename line $line\n";
}
