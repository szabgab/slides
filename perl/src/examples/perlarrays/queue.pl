#!/usr/bin/perl
use strict;
use warnings;

my @people = ("Foo", "Bar");
while (@people) {
    my $next_person = shift @people;
    print "$next_person\n"; # do something with this person

    print "Type in more people:";
    while (my $new = <STDIN>) {
        chomp $new;
        if ($new eq "") {
            last;
        }
        push @people, $new;
    }
    print "\n";
}

