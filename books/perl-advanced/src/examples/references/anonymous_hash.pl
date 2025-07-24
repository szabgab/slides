#!/usr/bin/perl
use strict;
use warnings;

my $phones_ref = {
    Foo   => 123,
    Bar   => 456,
    Moo   => 789,
};

print "$phones_ref->{Foo}\n";   # 123

