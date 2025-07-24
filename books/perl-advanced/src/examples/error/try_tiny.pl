#!/usr/bin/perl
use strict;
use warnings;

use Try::Tiny;

my $mode = shift or die "Usage: $0 good|bad|ugly\n";


my $answer;
try {
    $answer = code($mode);
    print "Answer received\n";
} catch {
    chomp $_;   # not $@
    if ($_ eq 'bad code') {
        warn "exception '$_' received\n";
    } else {
        warn "Unexpected exception '$_' received\n";
        die $_;
    }
};
if (defined $answer) {
    print "The answer is $answer\n";
}



sub code {
    my $mode = shift;
    print "code: $mode\n";
    if ($mode eq 'bad') {
        die "bad code\n";
    } elsif ($mode eq 'ugly') {
        die 'Some other error';
    } else {
        return 42;
    }
}

