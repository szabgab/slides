use strict;
use warnings;

use Test::More tests => 1;
use Expect;


my $exp   = Expect->new( "$^X examples/expect/random.pl" );
my $val;
$exp->expect(
    2,
    [ "abc" => sub { $val = 1; } ],
    [ "def" => sub { $val = 1; } ],
);
ok $val;

