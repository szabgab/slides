use strict;
use warnings;

use FindBin qw($Bin);
use lib $Bin;

use Test::More;
plan tests => 1;

use MyWebAPI;

my $w = MyWebAPI->new;

is_deeply $w->count_strings('Beyonce', 'Miley Cyrus'), 
    {
        'Beyonce'     => 26,
        'Miley Cyrus' => 3,
    };
