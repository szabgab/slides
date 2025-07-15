use strict;
use warnings;

use Test::More;
my $tests;

plan tests => 5;

use_ok('Point3D');

{
    my $p = Point3D->new(x => 23, y => 42, z => 19);
    isa_ok($p, 'Point3D');
    isa_ok($p, 'Point');

    is $p->x, 23, 'x';
    is $p->z, 19, 'z';
}



