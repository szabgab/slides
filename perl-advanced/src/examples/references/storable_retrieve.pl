#!/usr/bin/perl
use strict;
use warnings;

use Storable qw(retrieve);

my $data = retrieve 'frozen.data' or die;
print "Foo: $data->{phones}{Foo}\n"; # Foo: 123
print "Bar: $data->{phones}{Bar}\n"; # Bar: 345
print "Baz: $data->{phones}{Baz}\n"; # Baz: 678
