#!/usr/bin/perl
use strict;
use warnings;

use Test::More tests => 1;
use LWP::Simple;

my $home = get 'http://localhost:8080/xx';
ok $home, 'There is a response';
