#!/usr/bin/perl
use strict;
use warnings;

use Data::Dumper qw(Dumper);

my $ini = {
    'name' => {
            Foo => 123,
            Bar => 456,
    }
};

my $other_ini = { %{ $ini } };
print "$ini->{name}{Foo}\n";          # 123
print "$other_ini->{name}{Foo}\n";    # 123

$ini->{phone}{Baz} = 678;
print "$ini->{phone}{Baz}\n";         # 678
print "$other_ini->{phone}{Baz}\n";   # undef as expected
print Dumper $ini, $other_ini;

$ini->{name}{Foo} = 999;
print "$ini->{name}{Foo}\n";          # 999
print "$other_ini->{name}{Foo}\n";    # 999 !!!!
print Dumper $ini, $other_ini;

