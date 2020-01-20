#!/usr/bin/perl
use strict;
use warnings;

# examples/files/apache_access.log

my $file = shift
    or die "Usage: $0 FILENAME\n";
open my $fh, '<', $file or die "Could not open '$file': $!";

my %count;
while (my $line = <$fh>) {
    chomp $line;
    my $length = index ($line, " ");
    my $ip = substr($line, 0, $length);
    $count{$ip}++;   
}

foreach my $ip (keys %count) {
    print "$ip   $count{$ip}\n";
}

