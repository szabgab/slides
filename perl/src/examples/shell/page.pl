use strict;
use warnings;

if (not @ARGV) {
    die "Usage: $0 command    to page the output of the given command \n";
}

my $SIZE = 10;
my $cnt = $SIZE;
open my $ph, '-|', "@ARGV" or die;
while (my $line = <$ph>) {
    print $line;
    $cnt--;
    if ($cnt <= 0) {
        print "---";
        my $in = <STDIN>;
        chomp $in;
        if ($in eq ' ') {
            $cnt = $SIZE;
        } elsif ($in eq 'q') {
            last;
        } else {
            $cnt = 1;
        }
    }
}
close $ph;