#!/usr/bin/perl
use strict;
use warnings;


my %x = (
    foo    => 1,
    bar    => 2,
    baz    => 3,
    zoo    => 6,
    foobar => undef,
    moose  => undef,
);
my %y = (
    foo    => 1,
    bar    => 4,
    moo    => 5,
    zoo    => undef,
    foobar => 9,
    moose  => undef,
);

my @report = compare_hashes(\%x, \%y);
print join "\n", @report;
print "\n";


sub compare_hashes {
    my ($first, $second) = @_;
    my @report;
    foreach my $k (keys %{ $first }) {
        if (not exists $second->{$k}) {
            push @report, "The key '$k' does not exist in second hash";
        } elsif (not defined $first->{$k} and not defined $second->{$k}) {
            # ok, neither is defined
        } elsif (defined $first->{$k} and not defined $second->{$k}) {
            push @report,
                "The value of '$k' is '$first->{$k}' in the first hash"
                . " and undef in the second hash";
        } elsif (not defined $first->{$k} and defined $second->{$k}) {
            push @report,
                "The value of '$k' is '$second->{$k}' in the second hash"
                . " and undef in the first hash";
        } elsif ($first->{$k} ne $second->{$k}) {
            push @report,
                "The value of '$k' differs: '$first->{$k}' and '$second->{$k}'";
        }
    }
    foreach my $k (keys %{ $second }) {
        if (not exists $first->{$k}) {
            push @report, "The key '$k' does not exist in first hash";
        }
    }
    return @report;
}


