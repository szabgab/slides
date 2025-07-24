use strict;
use warnings;
use Test::More;

plan tests => 1;

use Cwd qw(abs_path);
use File::Basename qw(dirname);
use lib dirname(abs_path($0)) . '/lib';

use WWW::Mechanize;
diag $WWW::Mechanize::VERSION;
is $WWW::Mechanize::VERSION, 'fake';
