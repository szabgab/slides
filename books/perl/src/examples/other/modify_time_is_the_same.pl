use strict;
use warnings;
use feature 'say';
use Time::HiRes qw(sleep time stat);

{
    open(my $fh, '>', 'first.txt');
    $fh->flush;
    close $fh;
}

say "before ", time;
#sleep(0.0006);
say "after  ", time;

{
    open(my $fh, '>', 'second.txt');
    $fh->flush;
    close $fh;
}

my $first = (stat('first.txt'))[9];
my $second = (stat('second.txt'))[9];
say "first  $first";
say "second $second";
say $first == $second ? "same" : "different";

