use strict;
use warnings;
use 5.010;

use Test::More;
use Test::Selenium::Remote::Driver;
use Selenium::Remote::WDKeys qw(KEYS);


if (not Test::Selenium::Remote::Driver->server_is_running()) {
    plan skip_all => 'The Selenium server must be running for this test';
}

plan tests => 1;

my $url = 'http://localhost:8080/'; 
my $s = Test::Selenium::Remote::Driver->new(
    default_finder => 'css',
);


subtest jquery => sub {
    plan tests => 10;
    $s->get_ok($url);
    $s->click_element_ok('#jquerycalc');
    $s->title_is('JQuery based Calculator', 'title');
    $s->type_element_ok('input[name=a]', 19);
    $s->type_element_ok('input[name=b]', 23);
    $s->element_text_is('#result', 'Result:', 'result');
    sleep 3;

    $s->click_element_ok('#addstr');
    $s->element_text_is('#result', 'Result: 1923');
    sleep 3;

    $s->click_element_ok('#addnum');
    $s->element_text_is('#result', 'Result: 42');
    sleep 3;
};

$s->quit;

