use strict;
use warnings;

use Test::MockTime qw(set_absolute_time restore_time);
use Test::More;

use MyDaily qw(message);

diag time;

set_absolute_time('1970-03-01T03:00:00Z');
is message(), 'Welcome to Perl';

set_absolute_time('1970-04-01T03:00:00Z');
is message(), 'Welcome to Python';

diag time;
sleep(2);

diag time;
restore_time();
diag time;

done_testing;
