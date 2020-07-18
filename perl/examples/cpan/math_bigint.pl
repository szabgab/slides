#!/usr/bin/perl
use strict;
use warnings;

use Math::BigInt;
my $x = Math::BigInt->new("1234567890");
my $y = Math::BigInt->new("8234567890");

$x->badd($y);
print $x->bstr, "\n";         # 9469135780

