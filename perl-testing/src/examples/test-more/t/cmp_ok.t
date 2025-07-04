use strict;
use warnings;

use Test::More tests => 2;
use MyTools qw(wait_for_input_with_timeout);

my $start = time;
wait_for_input_with_timeout(3);
my $end = time;

cmp_ok $end - $start, ">=", 2, "process was waiting at least 2 secs";
cmp_ok $end - $start, "<=", 3, "process was waiting at most 3 secs";


