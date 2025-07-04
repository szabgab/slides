#!/usr/bin/perl
use strict;
use warnings;

use CGI;

my $q = CGI->new;

print $q->header;
print '<h1 align="center">';
my $a = $q->param('a') || 0;
my $b = $q->param('b') || 0;
print $a + $b;
print "</h1>\n";
