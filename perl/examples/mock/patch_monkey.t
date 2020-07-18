use strict;
use warnings;

use FindBin qw($Bin);
use lib $Bin;
use Monkey;

use Test::More tests => 5;

my $m = Monkey->new(10);
is $m->bananas, 10, 'bananas';

{
    my $eat;
    no warnings 'redefine';
    local *Monkey::eat = sub { $eat = 1;};
    ok $m->is_hungry, 'is_hungry';
    ok $eat, 'eat called';
}

is $m->bananas, 10, 'bananas';
$m->eat;
is $m->bananas, 9, 'bananas';

