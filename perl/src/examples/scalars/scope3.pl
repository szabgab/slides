#!/usr/bin/perl
use strict;
use warnings;

my $fname = "Foo";
print "$fname\n";        # Foo

{
    print "$fname\n";    # Foo

    my $fname  = "Other";
    print "$fname\n";    # Other
}
print "$fname\n";        # Foo


