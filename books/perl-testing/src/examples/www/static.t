#!/usr/bin/perl
use strict;
use warnings;

use Test::More tests => 1;
use LWP::Simple qw(get);

my $home = get 'http://localhost:8080/';
ok $home, 'There is a response';
