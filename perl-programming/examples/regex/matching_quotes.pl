#!/usr/bin/perl
use strict;
use warnings;

my $filename = 'sentences.txt';

my $content = slurp($filename);

if ($content =~ /<.*>/) {
    print "$&\n";
    print "-----------\n";
}

# If we want the smallest:
if ($content =~ /<[^>]*>/) {
    print "$&\n";
    print "-----------\n";
}

# If we want the biggest
if ($content =~ /<.*>/s) {
    print "$&\n";
    print "-----------\n";
}


sub slurp {
    my $file = shift;
    open my $fh, '<', $file or die "Could not open '$file' $!";
    local $/ = undef;
    my $all = <$fh>;
    close $fh;
    return $all;
}
