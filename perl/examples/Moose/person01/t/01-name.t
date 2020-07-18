use strict;
use warnings;
use v5.10;

use Test::More tests => 5;

use Person;

my $p = Person->new;
isa_ok($p, 'Person');

is($p->name('Foo'), 'Foo', 'setter');
is($p->name, 'Foo', 'getter');

my $o = Person->new( name => 'Bar' );
isa_ok($o, 'Person');
is($o->name, 'Bar');

