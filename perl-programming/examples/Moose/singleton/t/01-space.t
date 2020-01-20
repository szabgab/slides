use strict;
use warnings;

use Test::More;
plan tests => 2;

use Games::Spacefight;

my $game = Games::Spacefight->new;
isa_ok($game, 'Games::Spacefight');

my $game2 = Games::Spacefight->new;
is $game2, $game, 'Singleton';


