#!/usr/bin/perl
use strict;
use warnings;

while (my $number = <STDIN>) {

    # This solution only check is the string consists of characters
    # used in as Roman numbers but does not check if the number is
    # actually a valid number. (e.g. IVI is not valid)
    # I yet to see a definition on how to validate a Roman number.
    if (is_roman($number)) {
        print "Roman number\n";
    }
}

sub is_roman    { $_[0] =~ /^[IVXLCDM]+$/    }

sub is_roman2   { $_[0] =~ /^
    (M{0,4})
    (CM|CD|D?C{0,3})
    (XL|XC|L?X{0,3})
    (IV|IX|V?I{0,3})
    $/x  }

