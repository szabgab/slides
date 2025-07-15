use strict;
use warnings;
use v5.10;

use Test::More tests => 12+2+2;
use Test::Exception;

use Employee;

my $e = Employee->new;
isa_ok($e, 'Employee');

is($e->name('Foo'), 'Foo', 'setter');
is($e->name, 'Foo', 'getter');

is($e->sex('m'), 'm', 'set m');
is($e->sex, 'm',      'get m');
is($e->sex('f'), 'f', 'set f');
is($e->sex, 'f',      'get f');

is($e->sex('M'), 'm', 'set M');
is($e->sex, 'm',      'get m');

is($e->sex('male'), 'm', 'set male');
is($e->sex, 'm',      'get m');
throws_ok { $e->sex('other') }
    qr{Attribute \(sex\) does not pass the type constraint because:},
   'sex is f or m';


is($e->employer('Acme Corporation'), 'Acme Corporation', 'set employer');
is($e->employer, 'Acme Corporation', 'get employer');


use Person;
my $p = Person->new(employee => 'Acme Corp');
isa_ok($p, 'Person');
throws_ok { $p->employee }
    qr{Can't locate object method "employee" via package "Person"},
    'no employee method';

