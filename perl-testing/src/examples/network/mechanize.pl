#!/usr/bin/perl
use strict;
use warnings;
use 5.010;

use WWW::Mechanize;
my $w = WWW::Mechanize->new();
$w->get('http://localhost:5000/');
say $w->content;

