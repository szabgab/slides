use strict;
use warnings;
use v5.10;

use Test::More tests => 12;
use Test::Exception;

use Person;

my $p = Person->new;
isa_ok($p, 'Person');

is($p->name('Foo'), 'Foo', 'setter');
is($p->name, 'Foo', 'getter');

is($p->sex('m'), 'm', 'set m');
is($p->sex, 'm',      'get m');
is($p->sex('f'), 'f', 'set f');
is($p->sex, 'f',      'get f');

is($p->sex('M'), 'm', 'set M');
is($p->sex, 'm',      'get m');

is($p->sex('male'), 'm', 'set male');
is($p->sex, 'm',      'get m');
throws_ok { $p->sex('other') }
    qr{Attribute \(sex\) does not pass the type constraint because:};
