#!/usr/bin/perl
use strict;
use warnings;

use Test::More tests => 2;
use Test::HTML::Tidy;
use LWP::Simple qw(get);


my $home = get 'http://localhost:8080/';
ok $home, 'There is a response';
html_tidy_ok $home, 'HTML OK';

