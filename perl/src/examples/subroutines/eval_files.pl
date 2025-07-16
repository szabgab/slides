#!/usr/bin/perl
use strict;
use warnings;

my @files = ('abc.txt', $0);

foreach my $file (@files) {
    eval {
        process($file);
        print "   processing of $file done\n";
    };
    if ($@) {
        my $err = $@;
        chomp $err;
        warn "Error seen: $err";
    }
}

sub process {
    my ($file) = @_;
    open my $fh, '<', $file or die "Could not open '$file' $!";
    local $/ = undef;
    my $all = <$fh>;
    close $fh;
    print "Size of $file: ", length($all), "\n";
}
