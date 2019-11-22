#!/usr/bin/env perl
use v5.10;
use strict;
use warnings;

say $ENV{PATH};

for my $name (sort keys %ENV) {
    say $name;
}

$ENV{LANG} = 'Klingon';

