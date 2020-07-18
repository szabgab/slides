#!/usr/bin/perl
use strict;
use warnings;

use Expect;
use Test::More;

my @sets = (
    ['23+7',   30],
    ['11+1',   10],
    ['2*21',   42],
);

plan tests => 1 + 3 * scalar @sets;
 
my $e = Expect->new;
$e->log_stdout(0);
$e->raw_pty(1);
$e->spawn("bc") or BAIL_OUT("Could not start bc");

my $warranty;
$e->expect(1, ["warranty'\." => sub { $warranty = 1; }]);
ok $warranty, 'warranty';

foreach my $set (@sets) {
    $e->send("$set->[0]\n");
    ok($e->expect(1, $set->[0]), 'echo');
    ok($e->expect(1, -re => '\d+'), 'numbers received');
    is($e->match, $set->[1], "expected value of " . $set->[0]);
}

$e->send("quit\n");

