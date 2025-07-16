#!/usr/bin/perl
use strict;
use warnings;

use Getopt::Long qw(GetOptions);

my $color;
my $filename = "examples/colors.txt";
my $force;
GetOptions(
        "color=s"    => \$color,
        "filename=s" => \$filename,
        "force"      => \$force,
) or exit;

open(my $fh, "<", $filename)
    or die "Could not open '$filename' for reading: $!";

my @colors = <$fh>;
chomp @colors;

if ($color and not $force) {
    my $valid_color;
    foreach my $c (@colors) {
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
    foreach my $i (0..$#colors) {
        print "$i) $colors[$i]\n";
    }
    my $num = <STDIN>;
    chomp($num);
    if (defined $colors[$num]) {
        $color = $colors[$num];
    } else {
        print "Bad selection\n";
        exit;
    }
}

print "The selected color is $color\n";

