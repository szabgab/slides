#!/usr/bin/perl 
use strict;
use warnings;

use 5.010;

my $value = <STDIN>;
chomp $value;

given($value) {
    when(3) { say "Three"; }
    when(7) { say "Seven"; }
    when(9) { say "Nine"; }
    default { say "Non of the expected values"; }
}

given($value) {
    when(/^\d+$/)            { say "digits only"; }
    when(/^\w+$/)            { say "Word characters"; }
    when(/^[a-zA-Z0-9.-]+$/) { say "Domain namish"; }
    default { say "Non of the expected"; }
}


given($value) {
    when(10) {
        say "Number 10";
    }
    when([11, 23, 48]) {
        say "In the list";
    }
    when($_ < 21) {
        say "under 21";
    }
    when(/^\d+$/) {
        say "digits only";
    }
    when(\&is_number) {
        say "Is number";
    }
    default {
        say "None of the above";
    }
}

sub is_number {
    return $_[0] =~ /\d/ and $_[0] =~ /^[+-]?\d*\.\d*$/;
}

