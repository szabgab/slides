use strict;
use warnings;

use Test::More;

use Mock::Sub no_warnings => 1;
my $mock;
my $rand;
BEGIN {
    $mock = Mock::Sub->new;
    $rand = $mock->mock('MyRandomApp::rand');
};

use MyRandomApp qw(dice);

$rand->return_value(0.023);
is dice(10), 1;

$rand->return_value(0.72);
is dice(10), 8;

my $x = rand;
isnt $x, undef, 'The local rand() is not mocked';
cmp_ok $x, '<', 1;
cmp_ok $x, '>=', 0;
diag $x;

is $rand->called_count, 2, 'How many times rand() was called in MyRandomApp';

done_testing;

