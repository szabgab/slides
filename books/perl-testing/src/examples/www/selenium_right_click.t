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

subtest plain => sub {
    plan tests => 4;

    $s->get_ok($url);
    $s->title_is('Hello world');
    $s->click_element_ok('#other');
    $s->title_is('Hello world');

    #$s->switch_to_window('Other Window');
    #$s->title_is('Hello world');

};

sleep 5;

