use strict;
use warnings;

use Test::More;

eval 'use Test::Perl::Critic 1.02';
plan skip_all => 'Test::Perl::Critic 1.02 required' if $@;


ok 1;
done_testing;
