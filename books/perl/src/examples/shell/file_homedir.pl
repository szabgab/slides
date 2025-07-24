#!/usr/bin/perl 
use strict;
use warnings;

use File::HomeDir;
my $home = File::HomeDir->my_home;
my $docs = File::HomeDir->my_documents;

print "$home\n";
print "$docs\n";

