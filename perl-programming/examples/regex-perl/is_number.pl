#!/usr/bin/perl
use strict;
use warnings;

while (my $number = <STDIN>) {
    if (is_non_negative($number)) {
        print "non negative integer without +- sign\n";   # 0, 3, 7
    }
    if (is_integer($number)) {
        print "integer with optional +- sign\n";    # -1, +3
    }
    if (is_real($number)) {
        print "real number with decimal point\n";   # 3.1, 0.0,  .3,  2., -.7
    }
    if (is_exp($number)) {
        print "exponential format\n";               # .1e
    }
    if (is_exp2($number)) {
        print "exponential format (x)\n";           # .1e
    }
}
sub is_non_negative { $_[0] =~ /^\d+$/ }
sub is_integer      { $_[0] =~ /^[+-]?\d+$/ }
sub is_real         { $_[0] =~ /\d/ and $_[0] =~ /^[+-]?\d*\.?\d*$/}
sub is_exp          { $_[0] =~ /\d/ and $_[0] =~ /^[+-]?\d*\.?\d*(e[+-]?\d+)?$/}
sub is_exp2         { $_[0] =~ /\d/ and $_[0] =~ /^
            [+-]?            # optional + or - sign 
            \d*              # 0 or more digits before the decimal point
            \.?              # optional decimal point
            \d*              # 0 or more digits after the decimal point
            (e[+-]?\d+)?     # optional "e" followed by an integer number
            $/x}
