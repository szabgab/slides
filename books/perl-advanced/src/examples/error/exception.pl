#!/usr/bin/perl
use strict;
use warnings;

use English qw( -no_match_vars ) ;
use Carp qw(croak carp);
use Lottery qw(add_lottery_numbers);

# Catching exceptions
eval {
    add_lottery_numbers(@ARGV);
};
if ($EVAL_ERROR) {
    if (Number::Missing->caught) {
        print "$EVAL_ERROR\n";
        print "Usage: $0 NUMBERs  (at least 2 numbers are needed)\n";
        exit;
    }
    if (Number::Small->caught() or Number::Big->caught) {
        print "$EVAL_ERROR\n";
        print "Numbers must be between 1-90\n";
        exit;
    }

    # error that I don't know how to handle:
    croak $EVAL_ERROR;
}
print "Number was ok\n";


