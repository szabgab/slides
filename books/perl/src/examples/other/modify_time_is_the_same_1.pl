use strict;
use warnings;
use feature 'say';
use Time::HiRes qw(stat);

{
    open(my $fh, '>', 'first.txt');
}
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

