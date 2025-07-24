#!/usr/bin/perl
use strict;
use warnings;

{
    my $counter = 0;
    sub inc {
        $counter++;
        return $counter;
    }
}

print inc(), "\n";
print inc(), "\n";
print inc(), "\n";
print inc(), "\n";

