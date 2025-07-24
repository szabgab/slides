#!/usr/bin/env perl
use strict;
use warnings;


use Spreadsheet::ParseExcel::Simple qw();
my $xls = Spreadsheet::ParseExcel::Simple->read("spreadsheet.xls");
foreach my $sheet ($xls->sheets) {
    while ($sheet->has_data) {
        my @data = $sheet->next_row;
        print join "|", @data;
        print "\n";
    }
}

