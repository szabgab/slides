#!/usr/bin/perl
use strict;
use warnings;

my $w;

if ($^O eq 'MSWin32') {
    require Win32::IE::Mechanize;
    $w = Win32::IE::Mechanize->new( visible => 1 );
} else {
    require WWW::Mechanize;
    $w = WWW::Mechanize->new();
}

my $url = "http://pti/";

$w->get( $url );
sleep(2) if $^O eq 'MSWin32';

$w->follow_link(text => 'Services');
sleep(2) if $^O eq 'MSWin32';

printf "Title: %s\n",  $w->title;

foreach my $link ($w->find_all_links()) {
    printf "%s      %s\n", $link->url, $link->text;
}

$w->follow_link(text_regex => qr/QA/);

print "-"x80, "\n";
print $w->content;

