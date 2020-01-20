#!/usr/bin/perl
use strict;
use warnings;

my $file = "examples/files/apache_access.log";
open my $fh, '<', $file or die "Could not open '$file': $!";


my $local  = 0;
my $remote = 0;
while (my $line = <$fh>) {
    my $length = index ($line, " ");
    my $ip = substr($line, 0, $length);
    if ($ip eq "127.0.0.1") {
        $local++;
    } else {
        $remote++;
    }
}

print "Local: $local Remote: $remote\n";

