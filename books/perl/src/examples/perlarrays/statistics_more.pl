#!/usr/bin/perl
use strict;
use warnings;


my @data = <STDIN>;
chomp @data;

@data = sort { $a <=> $b } @data;


if (not @data) {
    print "No values were given\n";
    exit;
}

my $total = 0;
foreach my $v (@data) {
    $total += $v;
}

my $average = $total / @data;
my $median = @data % 2        ? $data[(@data-1)/2]  
           :                  ($data[@data/2-1]+$data[@data/2])/2
           ;

my $sqtotal = 0;
foreach my $v (@data) {
    $sqtotal += ($average-$v) ** 2;
}
my $std = ($sqtotal / @data) ** 0.5;

print "Min: $data[0]   Max: $data[-1]   Total: $total   count: " 
      . @data . "  Average: $average\n";
print "Median: $median   $sqtotal Standard deviation: $std\n";

