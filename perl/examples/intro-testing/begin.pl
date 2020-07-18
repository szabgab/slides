#!/usr/bin/perl
use strict;
use warnings;

use Test::More;
use Big::Qqrq;
my $tests;
plan tests => $tests;


{
   my $q = Big::Qqrq->new();
   isa_ok($q, 'Big::Qqqrq');
   is($q->sound_level(4), 4);
   BEGIN { $tests += 2; }
}

for (1..7) {
	ok(1);
   BEGIN { $tests += 7; }
}
{
   my $q = Big::Qqrq->new();
   is($q->sound_type('harsh'), 'harsh');
   BEGIN { $tests += 1; }
}






