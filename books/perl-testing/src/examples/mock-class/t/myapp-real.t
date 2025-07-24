use strict;
use warnings;
use Test::More;

use MySalary;
is MySalary::get_salary('Foo'), 100;

done_testing;

