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
my $driver = Test::Selenium::Remote::Driver->new;

subtest plain => sub {
    plan tests => 4;
    $driver->get_ok($url);
    $driver->title_is('Hello world', 'title');

    $driver->body_text_contains('Our languages');
    $driver->content_contains('<h1>Our languages</h1>');

};

