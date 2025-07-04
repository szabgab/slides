use strict;
use warnings;


my $hidden = 1 + int(100 * rand);

while (1) {
    print "Guess: ";
    my $guess = <STDIN>;
    if ($guess < $hidden) {
        print "Too small\n";
        next;
    }
    if ($guess > $hidden) {
        print "Too big\n";
        next;
    }
    print "Found\n";
    last;
}
