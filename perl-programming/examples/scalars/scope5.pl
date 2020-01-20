#!/usr/bin/perl
use strict;
use warnings;

my $fname  = "Foo";
print "$fname\n";    # Foo

package Other;
use strict;
use warnings;

print "$fname\n";    # Foo
my $lname = 'Bar';
print "$lname\n";    # Bar


package main;

print "$fname\n";    # Foo
print "$lname\n";    # Bar

