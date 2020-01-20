use strict;
use warnings;
use 5.010;

use Test::More;
use Test::Selenium::Remote::Driver;
use Selenium::Remote::WDKeys qw(KEYS);


if (not Test::Selenium::Remote::Driver->server_is_running()) {
    plan skip_all => 'The Selenium server must be running for this test';
}

plan tests => 2;

my $url = 'http://localhost:8080/'; 
my $s = Test::Selenium::Remote::Driver->new(
    default_finder => 'css',
);

subtest plain => sub {
    plan tests => 10;
    $s->get_ok($url);
    $s->click_element_ok('#calculator');
    $s->title_is('Calculator Test page');
    $s->type_element_ok('input[name=a]', 19);
    $s->type_element_ok('input[name=b]', 23);
    sleep 3;
    $s->click_element_ok('input[name=submit]');
    sleep 3;
    $s->title_is('Result');
    $s->element_text_is('h1', 42);
    $s->go_back_ok;
    $s->go_back_ok;
    sleep 1;
};

subtest js => sub {
    plan tests => 16;
    $s->click_element_ok('#jscal');
    $s->title_is('JS Calculator');
    $s->type_element_ok('input[name=a]', 19);
    $s->type_element_ok('input[name=b]', 23);
    $s->content_unlike(qr/42/);
    $s->content_unlike(qr/1923/);
    $s->content_like(qr/Foo Bar written by javascript/);
    sleep 3;
    $s->click_element_ok('#addstr');
    $s->alert_text_is('1923');
    $s->accept_alert_ok;
    $s->content_unlike(qr/1923/);
    sleep 3;

    $s->click_element_ok('#addnum');
    $s->alert_text_is('42');
    $s->accept_alert_ok;
    $s->content_unlike(qr/42/);
    $s->go_back_ok;
};

$s->quit;
