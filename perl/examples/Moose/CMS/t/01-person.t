use strict;
use warnings;

use Test::More;
use Test::Exception;

plan tests => 6;

use_ok('CMS::Person');

{
    my $p = CMS::Person->new;
    isa_ok($p, 'CMS::Person');
    throws_ok { $p->fname('Foo') } qr{Cannot assign a value to a read-only accessor}, 'fname is read-only';
    dies_ok { $p->fname('Foo') } 'fname is read-only';
}

{
    my $p = CMS::Person->new(fname => 'Foo');
    isa_ok($p, 'CMS::Person');
    is $p->fname, 'Foo';
}

