#!/usr/bin/perl
use strict;
use warnings;

my %WARNS;
local $SIG{__WARN__} = sub {
    my $message = shift;
    return if $WARNS{$message}++;
    logger('warning', $message);
}

my $counter;
count();
print "$counter\n";
$counter = undef;
count();

sub count {
    $counter = $counter + 42;
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
