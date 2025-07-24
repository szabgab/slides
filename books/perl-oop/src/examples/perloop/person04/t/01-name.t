use strict;
use warnings;
use v5.10;

use Test::More tests => 8;
use Test::Exception;

use Person;

my $p = Person->new;
isa_ok($p, 'Person');

is($p->name('Foo'), 'Foo', 'setter');
is($p->name, 'Foo', 'getter');

is($p->sex('m'), 'm', 'set m');
is($p->sex('f'), 'f', 'set f');

throws_ok { $p->sex('male') }
    qr{Attribute \(sex\) does not pass the type constraint because:};
throws_ok { $p->sex('M') }
    qr{Attribute \(sex\) does not pass the type constraint because:};
throws_ok { $p->sex('other') }
    qr{Attribute \(sex\) does not pass the type constraint because:};
