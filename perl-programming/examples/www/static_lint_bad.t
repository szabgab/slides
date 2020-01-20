#!/usr/bin/perl
use strict;
use warnings;

use Test::More tests => 2;
use Test::HTML::Lint;
use LWP::Simple qw(get);

my $html = get 'http://localhost:8080/bad.html';
ok $html, 'There is a response';
html_ok $html, 'HTML OK';

