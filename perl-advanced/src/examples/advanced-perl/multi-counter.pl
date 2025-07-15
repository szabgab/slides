#!/usr/bin/perl 
use strict;
use warnings;

print counter('a'), "\n";  # 1
print counter('b'), "\n";  # 1
print counter('a'), "\n";  # 2
print counter('c'), "\n";  # 1
print counter('a'), "\n";  # 3
print counter('a'), "\n";  # 4
print counter('b'), "\n";  # 2

{
    my %counter;
    sub counter {
       my $id = shift;
       return ++$counter{$id};
    }
}
