use strict;
use warnings;

use Test::More;
use Test::Mock::Simple;
my $mock = Test::Mock::Simple->new(module => 'MyWebAPI');

my $w = MyWebAPI->new('http://www.dailymail.co.uk/');

$mock->add(get => sub {
    return 'Beyonce Miley Cyrus Miley
Cyrus';
});
is_deeply $w->count_strings('Beyonce', 'Miley Cyrus'),
    {
        Beyonce => 1,
        'Miley Cyrus' => 2,
    };

done_testing;
