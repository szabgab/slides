use strict;
use warnings;

use FindBin qw($Bin);
use lib $Bin;
use Monkey;

use Test::More tests => 4;

my $m = Monkey->new(10);
is $m->bananas, 10, 'bananas';
ok $m->is_hungry, 'is_hungry';
is $m->bananas, 10, 'bananas';
$m->eat;
is $m->bananas, 9, 'bananas';

