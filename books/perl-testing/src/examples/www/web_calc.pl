#!/usr/bin/perl
use strict;
use warnings;

use WWW::Mechanize;

my $url = 'http://localhost:8080';

my $mech = WWW::Mechanize->new;
$mech->get($url);

$mech->follow_link( text => 'calculator' );

$mech->submit_form(
    fields => {
       a => 23,
       b => 19,
    },
);
print $mech->content;


