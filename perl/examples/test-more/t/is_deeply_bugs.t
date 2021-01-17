use strict;
use warnings;

use MyBugs;
use Test::More tests => 3;

my %expected = (
    bugs     => 3,
    errors   => 6,
    failures => 8,
    warnings => 1,
);


my %a = fetch_data_from_bug_tracking_system(0);
is_deeply( \%a, \%expected, "Query 0" );

my %b = fetch_data_from_bug_tracking_system(1);
is_deeply( \%b, \%expected, "Query 1" );

my %c = fetch_data_from_bug_tracking_system(2);
is_deeply( \%c, \%expected, "Query 2" );


