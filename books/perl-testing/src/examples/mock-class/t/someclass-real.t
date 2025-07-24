use strict;
use warnings;
use Test::More;

use SomeClass;

my $obj = SomeClass->new;
isa_ok $obj, 'SomeClass';

is $obj->name, undef;
is $obj->name('Apple'), 'Apple';
is $obj->name, 'Apple';

is $obj->double(3), 6;

done_testing;
