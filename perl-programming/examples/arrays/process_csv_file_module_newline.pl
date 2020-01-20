#!/usr/bin/perl
use strict;
use warnings;

use Text::CSV;

my $file = 'process_csv_file_module.csv';
if (defined $ARGV[0]) {
    $file = $ARGV[0];
}

my $csv = Text::CSV->new ({
    binary    => 1,
    auto_diag => 1,
    sep_char  => ';'
});

 
my $sum = 0;
open(my $data, '<:encoding(utf8)', $file) or die "Could not open '$file'\n";
while (my $fields = $csv->getline( $data )) {
    $sum += $fields->[2];
}
print "$sum\n";

