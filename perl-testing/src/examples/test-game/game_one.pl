use strict;
use warnings;


my $hidden = 1 + int(100 * rand);
#print "Debug '$hidden'\n";

print "Guess: ";
my $guess = <STDIN>;
chomp $guess;
if ($guess < $hidden) {
    print "Too small ($guess)\n";
} elsif ($guess > $hidden) {
    print "Too big ($guess)\n";
} else {
    print "Found\n";
}
