#!/usr/bin/perl
use strict;
use warnings;

my %count;

my %length = (
     A => 3,
     B => 4,
     C => 6,
     D => 5,
);

my $filename = "examples/hashes/variable_width_fields.log";
if ($ARGV[0]) {
    $filename = $ARGV[0];
}

open my $data, '<', $filename or die "Could not open '$filename' $!";

LINE:
while (my $line = <$data>) {
    chomp $line;
    if (substr($line, 0, 1) eq "#") {
        next;
    }
    my $cmds = substr($line, 16, -16);
    while ($cmds) {
        my $c = substr($cmds, 0, 1, "");
        if (not defined $length{$c}) {
            warn "....";
            next LINE;
        }
        my $cmd = substr($cmds, 0, $length{$c}, "");
 
        $count{$c}++;
        print "$c : $cmd\n";
    }
}

print "-" x 80, "\n";
foreach my $c (keys %count) {
    print "$c  $count{$c}\n";
}

