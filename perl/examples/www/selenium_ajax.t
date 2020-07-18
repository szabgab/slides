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
    plan tests => 15;
    $s->get_ok($url);
    $s->click_element_ok('#ajaxcalc');
    $s->title_is('Ajax Calculator', 'title');
    $s->type_element_ok('input[name=a]', 19);
    $s->type_element_ok('input[name=b]', 23);
    $s->element_text_is('#result', '', 'result');
    sleep 2;

    $s->click_element_ok('#add');
    $s->element_text_is('#result', '42');
    sleep 2;

    $s->clear_element_ok('#a');
    $s->clear_element_ok('#b');
    $s->type_element_ok('#a', 2);
    $s->type_element_ok('#b', 5);
    $s->type_element_ok('#sleep', 3);
    $s->click_element_ok('#add');
    sleep 4;  # this one is really needed
    $s->element_text_is('#result', '7');
    sleep 2;
};

$s->quit;


