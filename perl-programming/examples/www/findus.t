use strict;
use warnings;
use utf8;

use Test::More;
use Test::WWW::Selenium;
use WWW::Selenium::Util qw(server_is_running);

my $browser_url = "http://neuffen-opac.customer.findus-internet-opac.de";
my $url         = "$browser_url/cgi-bin/findus.fcgi.pl?customer=neuffen";
#&_cookiecheck=2009-02-22-14-11-20
my $tests;

plan tests => $tests;

BAIL_OUT("No Selenium server found. Run it by typing selenium-rc") if not server_is_running;

my $sel = Test::WWW::Selenium->new( 
     host            => "localhost", 
     port            => 4444, 
     browser         => "*firefox",
     #browser         => "*chrome /usr/lib/firefox/firefox-bin",
     browser_url     => $browser_url,
     default_names   => 1,
);

my $title = qr/^Stadtbücherei Neuffen, Mediensuche$/;
{
    $sel->open_ok($url) or BAIL_OUT("Could not find the server");
    $sel->wait_for_page_to_load(5000);
    $sel->title_like($title);


#    diag $sel->get_body_text; # returns the text without the HTML tags
#    diag $sel->get_html_source; # returns the entire HTML source

    my @links = $sel->get_all_links(); # it returns the ids, but it seems to return one empty id anyway
#    diag Dumper \@links;
    BEGIN { $tests += 2; }
}

{
    $sel->click_ok('link=Leserkonto/Merkzettel');
    $sel->wait_for_page_to_load(5000);
    $sel->title_like($title);
    $sel->body_text_like(qr/Leserkonto abfragen/);

    $sel->click_ok('submit');
    $sel->wait_for_page_to_load(5000);
    $sel->title_like($title);
    $sel->body_text_like(qr/Leserkonto abfragen/);

    $sel->type_ok('lesernr', 123);
    $sel->type_ok('gebdat', 11);
    $sel->click_ok('submit');
    $sel->wait_for_page_to_load(5000);
    $sel->title_like($title);
    $sel->body_text_like(qr/Leserkonto abfragen/);
    $sel->body_text_like(qr/Leider stimmen Ihre Anmeldedaten nicht./);

    BEGIN { $tests += 3 + 3 + 6 }
}

{
    $sel->click_ok('link=Neuerwerbungen');
    $sel->wait_for_page_to_load(5000);
    $sel->title_like($title);
    $sel->body_text_like(qr/Alle \d+ neu beschafften Medien der letzten/);

#    $self->is_visble("Inhalt:");
    $sel->click_ok('link=Details hier');
    $sel->pause(1000);
    $sel->is_visible("Inhalt:");

    BEGIN { $tests += 3 + 2 }
}

