#!/usr/bin/perl
use strict;
use warnings;

my $filename = shift or die "Usage: $0 FILENAME\n";

open(my $fh, "<", $filename) or die "Could not open '$filename'\n";

my %score_of;
while (my $line = <$fh>) {
    chomp $line;
    my ($name, $score) = split /,/, $line;
    $score_of{$name} = $score;
}

foreach my $name (sort keys %score_of) {
    printf "%-10s %s\n", $name, $score_of{$name};
}
print "--------------------------\n";

foreach my $name (sort { 
                        $score_of{$b} <=> $score_of{$a} 
                       } keys %score_of) {
    printf "%-10s %s\n", $name, $score_of{$name};
}


