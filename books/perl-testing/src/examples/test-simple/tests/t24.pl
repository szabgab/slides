use strict;
use warnings;

use FindBin;
use lib "$FindBin::Bin/../lib";
use MySimpleCalc qw(sum);

my @tests;
BEGIN {
    my $file = "$FindBin::Bin/large_sum.txt";
    open my $fh, '<', $file or die "Could not open '$file': $!";

    while (my $line = <$fh>) {
        chomp $line;
        next if $line =~ /^\s*(#.*)?$/;
        my @data = split /\s*[,=]\s*/, $line;
        push @tests, \@data;
    }
}

use Test::Simple tests => scalar @tests;

foreach my $t (@tests) {
    my $expected = pop @$t;
    my $real     = sum(@$t);
    my $name     = join " + ", @$t;

    ok( $real == $expected, $name );
}

