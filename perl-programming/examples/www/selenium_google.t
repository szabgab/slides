use strict;
use warnings;

use Test::More tests => 5;
use Test::WWW::Selenium;

use WWW::Selenium::Util qw(server_is_running);

if (server_is_running) {
    my $sel = Test::WWW::Selenium->new( 
        host            => "localhost", 
        port            => 4444, 
        browser         => "*firefox",
        #browser         => "*firefox /usr/lib/firefox-3.0.6/firefox-bin",
        #browser         => "*chrome /usr/lib/firefox-3.0.6/firefox-bin",
        #browser         => "*chrome /usr/lib/firefox/firefox-bin",
        browser_url     => "http://www.google.com",
        default_names   => 1,
    );
    $sel->open_ok("http://www.google.com");
    $sel->wait_for_page_to_load(5000);
    $sel->title_like(qr/Google/);
sleep 5;
    $sel->type_ok( "q", "perl");
    $sel->click_ok("btnG");
    $sel->wait_for_page_to_load_ok(5000);
sleep 5;
    #$sel->title_like(qr/Google Search/);
    #diag $sel->get_body_text;
}


