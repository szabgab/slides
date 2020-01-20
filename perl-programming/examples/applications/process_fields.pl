#!/usr/bin/env perl
use strict;
use warnings;

use Text::CSV_XS qw();
use Data::Dumper qw(Dumper);

my $filename = shift or die "Usage: $0 FILENAME\n";
open(my $fh, "<", $filename) or die "Could not open '$filename': $!";

my $csv = Text::CSV_XS->new;

my $key = "Name";

my $header = <$fh>;
chomp $header;
$csv->parse($header);
my @header = $csv->fields;

my %data;

while (my $line = <$fh>) {
    chomp $line;
    $csv->parse($line);
    my @cols = $csv->fields;
    my %h;
    @h{@header} = @cols;

    $data{$h{$key}} = \%h;
}

print Dumper \%data;



