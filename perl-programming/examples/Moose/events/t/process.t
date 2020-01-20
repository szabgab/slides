use strict;
use warnings;
use 5.008;
use autodie;

use Test::More;
plan tests => 1;

use_ok('Process');

my $error;
open my $eh, '>', \$error;
my $p = Process->new(file => 't/files/input.txt', err => $eh);
$p->run;
diag $p->out;
diag $error;

