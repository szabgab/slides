#!/usr/bin/perl
use strict;
use warnings; 

my $s = "The black cat jumped from the green tree";

print index $s, "ac";                         # 6
print "\n";

print index $s, "e";                          # 2
print "\n";
print index $s, "e", 3;                       # 18
print "\n";

print index $s, "dog";                        # -1
print "\n";

print rindex $s, "e";                         # 39
print "\n";
print rindex $s, "e", 38;                     # 38
print "\n";
print rindex $s, "e", 37;                     # 33
print "\n";

