#!/usr/bin/perl T
use strict;
use warnings;

use CGI;
my $q = CGI->new;
print $q->header;
print "The CGI Works";

