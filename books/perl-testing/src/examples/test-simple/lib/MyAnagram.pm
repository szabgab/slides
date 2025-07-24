package MyAnagram;
use strict;
use warnings;

use Exporter qw(import);
our @EXPORT_OK = qw(is_anagram);

sub is_anagram {
    my ($x, $y) = @_;
    my $xx = join('', sort(split(//, $x)));
    my $yy = join('', sort(split(//, $y)));

    return $xx eq $yy;
}


1;

