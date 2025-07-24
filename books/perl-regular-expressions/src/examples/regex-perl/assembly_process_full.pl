#!/usr/bin/perl
use strict;
use warnings;

use File::Slurp qw(read_file write_file);


my %conversion = (
    R1  => 'R2',
    R2  => 'R3',
    R3  => 'R1',
    R12 => 'R21',
    R21 => 'R12',
);

replace(\%conversion, \@ARGV);

sub replace {
    my ($map, $files) = @_;

    my $regex = join "|", keys %$map;

    my $ts = time;

    foreach my $file (@$files) {
        my $data = read_file($file);
        $data =~ s/\b($regex)\b/$map->{$1}/g;
        rename $file, "$file.$ts";       # backup with current timestamp
        write_file( $file, $data);
    }
}


