use strict;
use warnings;

use Test::More;
use Test::Mock::Simple;
my $mock = Test::Mock::Simple->new(module => 'MyWebAPI');

my $w = MyWebAPI->new('http://www.dailymail.co.uk/');

$mock->add(get => sub {
    die 'Something went wrong';
});
is_deeply $w->count_strings('Beyonce', 'Miley Cyrus'),
    {
        Beyonce => 0,
        'Miley Cyrus' => 0,
    };


done_testing;
