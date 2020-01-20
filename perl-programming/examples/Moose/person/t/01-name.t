use strict;
use warnings;
use v5.10;

use Test::More tests => 10;
use Test::Exception;
use DateTime;


use_ok('Person');

my $p = Person->new;
isa_ok($p, 'Person');

is($p->name('Foo'), 'Foo', 'setter');
is($p->name, 'Foo', 'getter');

is($p->year(2000), 2000);
is($p->year, 2000);

throws_ok { $p->year('23 years old') } qr/Attribute \(year\) does not pass the type constraint/;


isa_ok($p->birthday( DateTime->new( year => 1988, month => 10, day => 7) ), 'DateTime');

isa_ok($p->birthday( DateTime->new( year => 2035, month => 10, day => 7) ), 'DateTime');

isa_ok($p->age, 'DateTime::Duration');
diag $p->age->years;

