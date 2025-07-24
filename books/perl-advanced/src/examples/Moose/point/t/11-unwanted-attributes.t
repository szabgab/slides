use strict;
use warnings;

use Test::More;
use Test::Exception;

plan tests => 8;

use_ok('Simple');
use_ok('Simple::Strict');

{
    my $s = Simple->new(fname => 'Foo', lname => 'Bar');
    isa_ok $s, 'Simple';
    lives_and { is $s->fname, 'Foo' } 'Simple fname';
}

{
    my $s = Simple::Strict->new(fname => 'Foo');
    isa_ok $s, 'Simple::Strict';
    is $s->fname, 'Foo', 'Simple::Strict fname';
}

{
    dies_ok { Simple::Strict->new(fname => 'Foo', lname => 'Bar') }
        'expected to die';
    like $@, qr/Found unknown attribute.* lname/, 'text of exception';
}


