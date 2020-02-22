use strict;
use warnings;

use Test::More tests => 3;
use Test::Deep;

use lib 'lib';
use MyBugs;

use Data::Dumper;

my $NUMBER = re('^\d+$');

my %expected = (
        bugs     => $NUMBER,
        errors   => $NUMBER,
        failures => $NUMBER,
        warnings => $NUMBER,
    );

#diag Dumper \%a;
for my $i (0..3) {
    my %a = fetch_data_from_bug_tracking_system($i);
    cmp_deeply(\%a, \%expected, 'hash is ok');
}


