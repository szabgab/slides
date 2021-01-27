#!/usr/bin/env perl
use strict;
use warnings;

my @names = qw(Foo Bar);
my @copy_names = @names;
$copy_names[0] = 'Baz';

print "$names[0]\n";       # Foo
print "$copy_names[0]\n";  # Baz

