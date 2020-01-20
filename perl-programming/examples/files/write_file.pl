#!/usr/bin/perl
use strict;
use warnings;

my $filename = "report.txt";
open my $fh, '>', $filename or die "Could not open file '$filename' $!";

my $title = "Report by: Foo Bar"; 
print $fh "$title\n";
print $fh "-" x length $title, "\n";
