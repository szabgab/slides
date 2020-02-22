#!/usr/bin/perl
use strict;
use warnings;

local $SIG{__WARN__} = sub {
    my $message = shift;
    logger('warning', $message);
};

my $total;
add();
print "$total\n";

sub add {
    $total = $total + rand();
}

# Use of uninitialized value in addition (+)
#    at examples/advanced/code_with_warnings.pl line 14.

sub logger {
    my ($level, $msg) = @_;
    if (open my $out, '>>', 'log.txt') {
        chomp $msg;
        print $out "$level - $msg\n";
    }
}
