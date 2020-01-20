#!/usr/bin/env perl
use strict;
use warnings;

=head1 DESCRIPTION

File have sections separated by empty lines
Each section has several   field = value entries like this:
Given a value of the name field print out all the values in this section

device   =    234234
name     =    Big
address  =    115.6.79.8
class    =    B

=cut

if (@ARGV != 2) {
    die "\n  Usage: $0 filename name\n  Try:   $0 examples/config.txt Big\n\n";
}
my ($filename, $name) = @ARGV;

open(my $fh, "<", $filename) or die "Could not open '$filename' $!";
my %data;
while (my $line = <$fh>) {
    chomp $line;
    if ($line =~ /^\s*$/ and %data) {
        if ($data{name} eq $name) {
            foreach my $k (keys %data) {
                printf "%-10s = %s\n", $k, $data{$k};
            }
            exit;
        }
        %data = ();
    } else {
        my ($field, $value) = split /\s*=\s*/, $line;
        $data{$field} = $value;
    }
}

