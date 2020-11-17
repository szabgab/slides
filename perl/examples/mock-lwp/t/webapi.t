use strict;
use warnings;

use Test::More;

use MyWebAPI;

my $w = MyWebAPI->new('http://www.dailymail.co.uk/');

diag explain $w->count_strings('Beyonce', 'Miley Cyrus');

is_deeply $w->count_strings('Beyonce', 'Miley Cyrus'),
    {
        'Beyonce'     => 26,
        'Miley Cyrus' => 3,
    };

done_testing;
