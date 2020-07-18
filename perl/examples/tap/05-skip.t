use strict;
use warnings;


use Test::More tests => 5;

ok(1, "works");
is(2+2, 4, "2+2 is 4, who would guess ?");

SKIP: {
	skip "" , 2;
	my $v = -1;
	is($v**0.5 , "i", "support imginary numbers");
	ok(0, "some other thing");
}

ok(1, "can work");
