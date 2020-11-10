use strict;
use warnings;
use 5.010;

use lib 'lib';
use MyTools qw(get_copyright get_copyright_broken);

say (get_copyright());
say (get_copyright_broken());
