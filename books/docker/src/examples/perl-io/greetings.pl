use 5.010;
use strict;
use warnings;

print "What is your name? ";
my $name = <STDIN>;
chomp $name;
say "Hello $name, how are you today?";
