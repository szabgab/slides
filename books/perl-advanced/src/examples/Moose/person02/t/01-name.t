use strict;
use warnings;
use v5.10;

use Test::More tests => 6;
use Test::Exception;

use Person;

my $p = Person->new;
isa_ok($p, 'Person');

is($p->name('Foo'), 'Foo', 'setter');
is($p->name, 'Foo', 'getter');

is($p->year(2000), 2000);
is($p->year, 2000);

my $def_err  = qr{Attribute \(year\) does not pass the type constraint because:};
my $home_err = qr{Validation failed for 'Int' with value 23 years ago};

throws_ok { $p->year('23 years ago') } qr{$def_err $home_err}, 'exception';

