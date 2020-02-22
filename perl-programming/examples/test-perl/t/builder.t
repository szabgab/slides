use strict;
use warnings;

use Test::More tests => 1;
use Test::Builder;
use Test::Builder::Module;

my $TMb = Test::More->builder;
diag $TMb;

my $TBM = Test::Builder::Module->builder;
diag $TBM;

my $TBn = Test::Builder->new;
diag $TBn;

ok 1;
