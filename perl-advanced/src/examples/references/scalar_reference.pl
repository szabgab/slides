#!/usr/bin/env perl
use strict;
use warnings;

my $name = "Foo";
my $name_ref = \$name;

print "$name_ref\n";  # SCALAR(0x562516e5f140)
print "$name\n";      # Foo
print "$$name_ref\n"; # Foo
