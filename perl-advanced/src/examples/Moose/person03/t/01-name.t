use strict;
use warnings;
use v5.10;

use DateTime;

use Test::More tests => 7;
use Test::Exception;

use Person;

my $p = Person->new;
isa_ok($p, 'Person');

is($p->name('Foo'), 'Foo', 'setter');
is($p->name, 'Foo', 'getter');

isa_ok(
  $p->birthday( DateTime->new( year => 1988, month => 4, day => 17) ),
  'DateTime');

my $d = $p->birthday;
isa_ok($d, 'DateTime');
is($d->year, 1988, 'year is correct');

my $default_err =
  qr{Attribute \(birthday\) does not pass the type constraint because:};
my $homemade_err =
  qr{Validation failed for 'DateTime' with value 1988};

throws_ok { $p->birthday( 1988 ) }
   qr{$default_err $homemade_err}, 'Year as birthday';
