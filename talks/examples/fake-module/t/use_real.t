use strict;
use warnings;
use Test::More;

plan tests => 1;

use WWW::Mechanize;
diag $WWW::Mechanize::VERSION;
like $WWW::Mechanize::VERSION, qr/^\d+\.\d+$/;
