use strict;
use warnings;

use Test::More;

use Test::Mock::Simple;
use MyWebAPI;

my $w = MyWebAPI->new('http://www.dailymail.co.uk/');

my $mock = Test::Mock::Simple->new(module => 'MyWebAPI');
#my $mock = Test::Mock::Simple->new(module => 'LWP::Simple');

$mock->add(get => sub {
    return 'Beyonce Beyonce Miley Cyrus';
});
is_deeply $w->count_strings('Beyonce', 'Miley Cyrus'),
    {
        'Beyonce'     => 2,
        'Miley Cyrus' => 1,
    };

$mock->add(get => sub {
    return 'Beyonce';
});
is_deeply $w->count_strings('Beyonce', 'Miley Cyrus'),
    {
        Beyonce => 1,
        'Miley Cyrus' => 0,
    };

$mock->add(get => sub {
    return '';
});
is_deeply $w->count_strings('Beyonce', 'Miley Cyrus'),
    {
        Beyonce => 0,
        'Miley Cyrus' => 0,
    };


done_testing;
