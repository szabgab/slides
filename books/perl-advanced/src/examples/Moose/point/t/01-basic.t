use strict;
use warnings;

use Test::More;
my $tests;

plan tests => $tests;


{
    use_ok('Sys::Net::Device');

    my $host = Sys::Net::Device->new;
    isa_ok($host, 'Sys::Net::Device');

    ok(!defined $host->name(), 'getter returns undef when the value is not set (no name yet)');
    is($host->name('Foo'), 'Foo', 'setter returns the newly set value');
    is($host->name, 'Foo', 'getter returns the new value');

    my @names = $host->get_card_names;
    is_deeply(\@names, [], 'no cards');
    $host->add_card('eth0');

    @names = $host->get_card_names;
    is_deeply(\@names, ['eth0'], '1 card');

    BEGIN { $tests += 7; }
}


