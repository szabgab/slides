#!/usr/bin/perl
use strict;
use warnings;

sub incrementer_generator {
    my ($inc) = @_;

    return sub {
        my $old = $_[0];
        $_[0] += $inc;
        return $old;
    }
}

my $inc19 = incrementer_generator(19);

my $x = 23;
my $old_value = $inc19->($x);
print "$x\n";
print "old after inc19: $old_value\n";


my $inc5 = incrementer_generator(5);
print "old after inc5: " . $inc5->($x) . "\n";
print "$x\n";

my $prev_value = $inc19->($x);
print "old after inc19: $prev_value\n";
print "$x\n";
