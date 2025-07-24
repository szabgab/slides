#!/usr/bin/perl
use strict;
use warnings;

use English qw( -no_match_vars ) ;

my $mode = shift or die "Usage: $0 good|bad|ugly\n";


my $answer;
eval {
    $answer = code($mode);
    print "Answer received\n";
};
if ($EVAL_ERROR) {    # $@
    chomp $EVAL_ERROR;
    if ($EVAL_ERROR eq 'bad code') {
        warn "exception '$EVAL_ERROR' received\n";
    } else {
        warn "Unexpected exception '$EVAL_ERROR' received\n";
        die $EVAL_ERROR;
    }
} else {
    print "The answer is $answer\n";
}



sub code {
    my $mode = shift;
    print "code: $mode\n";
    if ($mode eq "bad") {
        die "bad code\n";
    } elsif ($mode eq 'ugly') {
        die 'Some other error';
    } else {
        return 42;
    }
}

