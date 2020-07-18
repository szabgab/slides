#!/usr/bin/perl
use strict;
use warnings;

use Test::More tests => 8;
use Test::WWW::Mechanize;
#use Test::HTML::Tidy;

my $SERVER = 'http://localhost:8080';

my $url  = $SERVER;

my $mech = Test::WWW::Mechanize->new;
$mech->get_ok($url);
$mech->content_like( qr{Our languages}, 'content' );

$mech->follow_link_ok({ text => 'calculator' });
$mech->content_like( qr{Calculator}, 'start page ok' );

#html_tidy_ok( $mech->content, "html is tidy" );

$mech->submit_form(
    fields => {
       a => 23,
       b => 19,
    },
);
$mech->content_like( qr{<h1 align="center">42</h1>}, 'get 42' );

#html_tidy_ok( $mech->content, "result html is tidy" );
$mech->back;

my @comps = (
   [23, 19, 42],
   [1,   2,  3],
   [1,   -1, 0],
);

foreach my $c (@comps) {
   $mech->submit_form(
      fields => {
       a => $c->[0],
       b => $c->[1],
      },
   );
   $mech->content_like( 
        qr{<h1 align="center">$c->[2]</h1>},
        "$c->[0]+$c->[1]=$c->[2]");

   $mech->back;
}

