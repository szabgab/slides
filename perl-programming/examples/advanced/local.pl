#!/usr/bin/perl
use strict;
use warnings;

our $global = 100;
our $my = 200;
our $local = 300;
print_variables();
              # $global   100
              # $my       200
              # $local    300
set();
              # $global   1
              # $my       2
              # $local    3
# inside print_variables():
              # $global   1
              # $my       200
              # $local    3

print_variables();
              # $global   1
              # $my       200
              # $local    300

sub set {
    $global = 1;
    my $my = 2;
    local $local = 3;

    print "$global\n";
    print "$my\n";
    print "$local\n";
    print "---\n";

    print_variables();
}

sub print_variables {
    print "$global\n";
    print "$my\n";
    print "$local\n";
    print "---\n";
}
