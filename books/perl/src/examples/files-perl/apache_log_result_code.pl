#!/usr/bin/perl
use strict;
use warnings;

my $file = "examples/files/apache_access.log";
open my $fh, '<', $file or die "Could not open '$file': $!";


my $good    = 0;
my $bad     = 0;
my $invalid = 0;
while (my $line = <$fh>) {
    chomp $line;
    my $request = q( HTTP/1.1" );
    my $start = index ($line, $request);
    if ($start < 0) {
        $request = q( HTTP/1.0" );
        $start = index ($line, $request);
    }
    if ($start < 0) {
        #print "ERROR: Unrecognized Line: $line\n";
        $invalid++;
        next;
    }

    my $end = index($line, " ", $start + length($request));
    my $result = substr($line,
        $start + length($request),
        $end - $start - length($request));
        #print "$start, $end '$result'\n";
    if ($result eq "200") {
        $good++;
    } else {
        $bad++;
    }
}

print "Good: $good\n";
print "Bad:  $bad\n";
print "Invalid: $invalid\n";


# Disclaimer: this is not an optimal solution.
# We will see a much better one after learning functions, regular expressions
