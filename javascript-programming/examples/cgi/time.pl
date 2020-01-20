#!/usr/bin/perl
use strict;
use warnings;
use CGI;
print CGI->new->header;
print scalar localtime;

