#!/usr/bin/perl
use strict;
use warnings;

use Getopt::Long qw(GetOptions);

my $color;
my $filename = "examples/color_map.txt";
GetOptions(
        "color=s"    => \$color,
        "filename=s" => \$filename,
);

my %colors;

open(my $fh, "<", $filename)
    or die "Could not open '$filename' for reading: $!";

while (my $line = <$fh>) {
    chomp $line;
    my ($color_name, $letter) = split / /, $line;
    if ($colors{$letter}) {
        warn 
            sprintf "%s appears to be allocated to both %s and %s\n",
                $letter, $colors{$letter}, $color_name
    } else {
        $colors{$letter} = $color_name;
    }
}

if ($color) {
    my $valid_color;
    foreach my $c (values %colors) {
        if ($c eq $color) {
            $valid_color = 1;
            next;
        }
    }
    if (not $valid_color) {
        print "The color '$color' is not valid.\n";
        $color = '';
    }
}


if (not $color) {
    print "Please select a number:\n";
    foreach my $k (sort keys %colors) {
        print "$k) $colors{$k}\n";
    }
    my $letter = <STDIN>;
    chomp($letter);
    if ($colors{$letter}) {
        $color = $colors{$letter};
    } else {
        print "Bad selection\n";
        exit;
    }
}

print "The selected color is $color\n";

