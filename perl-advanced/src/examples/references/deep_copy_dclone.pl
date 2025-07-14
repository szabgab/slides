#!/usr/bin/perl
use strict;
use warnings;

use Storable qw(dclone);

my $ini = {
    'name' => {
            Foo => 123,
            Bar => 456,
    }
};

my $other_ini = dclone($ini);
print "$ini->{name}{Foo}\n";
print "$other_ini->{name}{Foo}\n";

$ini->{phone}{Baz} = 678;
print "$ini->{phone}{Baz}\n";
print "$other_ini->{phone}{Baz}\n"; #undef

$ini->{name}{Foo} = 999;
print "$ini->{name}{Foo}\n";          # 999
print "$other_ini->{name}{Foo}\n";    # 123
