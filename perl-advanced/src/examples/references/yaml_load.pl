#!/usr/bin/perl
use strict;
use warnings;

use YAML qw(LoadFile);
my $data = LoadFile('data.yml');
print "$data->{people}->{Foo}->{phone}\n";          # 123
print "$data->{people}->{Bar}->{phones}->[0]\n";    # 345
print "$data->{people}->{Baz}\n";                   # NA

