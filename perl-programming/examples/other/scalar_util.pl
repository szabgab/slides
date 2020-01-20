#!/usr/bin/perl
use strict;
use warnings;
use v5.10;

use Scalar::Util qw(dualvar isvstring refaddr reftype);

# my $q = dualvar 42, "What is the meaning of life?";
# say $q;
# say 0+$q;

my $v = v1.12.3;
#say $v;
say isvstring $v;

my $x = v1.2.3;
say isvstring $x;
say $x lt $v;
#my $s = "1.2";
#my $z = v$s;

# say defined refaddr [];

my $r = reftype undef;
#say reftype 'ddd';
