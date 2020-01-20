use strict;
use warnings;

use Test::More;
my $tests;

plan tests => $tests;

{
    use_ok 'Point';
    my $p = Point->new;
    isa_ok $p, 'Point';

    is $p->x(10), 10, 'set x';
    is $p->x, 10, 'get x';

    is $p->y(20), 20, 'set y';
    is $p->y, 20, 'get y';

    eval {$p->name("Foo");};
    like $@ , qr/Cannot assign a value to a read-only accessor/,
        'exception on assignment to ro method';

    is $p->set_name("Bar"), 'Bar', 'set_name';
    is $p->name, 'Bar', 'get name';

    BEGIN { $tests += 9; }
}

{
    my $p = Point->new(name => 'Foo');
    isa_ok $p, 'Point';
    is $p->name, 'Foo', 'get name';

    BEGIN { $tests += 2; }
}

