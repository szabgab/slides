#!/usr/bin/perl 
use strict;
use warnings;

use WWW::Mechanize;

my $mech = WWW::Mechanize->new;

$mech->get('http://perlmaven.com/');

$mech->follow_link( text_regex => qr/tutorial/ );

print $mech->content;


