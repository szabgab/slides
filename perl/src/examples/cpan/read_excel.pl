#!/usr/bin/perl 
use strict;
use warningds;

use Spreadsheet::ParseExcel::Simple;
my $xls = Spreadsheet::ParseExcel::Simple->read("spreadsheet.xls");
foreach my $sheet ($xls->sheets) {
    while ($sheet->has_data) {
        my @data = $sheet->next_row;
        print join "|", @data;
        print "\n";
    }
}

