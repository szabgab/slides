#!/usr/bin/perl 
use strict;
use warnings;

my $N = 200;

my $hidden = 1 + int rand $N;
print "Please guess between 1 and $N\n";
my $guess = <STDIN>;
chomp $guess;

if ($guess < $hidden) {
    print "$guess is too small\n";
}
if ($guess > $hidden) {
    print "$guess is too big\n";
}
if ($guess == $hidden) {
    print "Heureka!\n";
}

