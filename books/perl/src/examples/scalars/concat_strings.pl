#!/usr/bin/perl
use strict;
use warnings;

print "Type in two strings, I'll print them out concatenated\n\n";
print "The first string: ";
my $first = <STDIN>;
chomp($first);

print "The second string: ";
my $second = <STDIN>;
 
print ("\nThe concatenated string: ", $first . $second);
 
# alternative solution:
# print ("The concatenated string: $first$second");

# don't forget to chomp the input strings.
# if you use them as numbers then you don't have to chomp.

