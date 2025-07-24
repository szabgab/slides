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
    plan tests => 5;

    $s->get_ok($url);
    $s->title_is('Hello world');
    $s->click_element_ok('#other');
    $s->title_is('Hello world');

    #$s->switch_to_window('Other Window');
    #$s->title_is('Hello world');

    my $handles = $s->get_window_handles;
    diag explain $handles;
    my @titles;
    foreach my $h (@$handles) {
        $s->switch_to_window($h);
        diag $s->get_title;
        push @titles, $s->get_title;
    }

    foreach my $t (@titles) {
        $s->switch_to_window($t);
        diag $s->get_title;
    }
};

sleep 5;
