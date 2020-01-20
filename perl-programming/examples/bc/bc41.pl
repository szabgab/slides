#!/usr/bin/perl
use strict;
use warnings;

use Expect;
use Test::More tests => 5;

my $e = Expect->new;
$e->log_stdout(0);
#$e->raw_pty(1);
$e->spawn("bc") or BAIL_OUT("Cannot run bc");

my $warranty;
$e->expect(1, ["warranty'\." => sub { $warranty = 1; }]);
ok $warranty, 'warranty';

$e->send("23+7\n");
ok($e->expect(1, -re => '\d+\+\d+'), 'echo expression');
is($e->match, '23+7', 'input');

ok($e->expect(1, -re => '\d+'), 'data received');
is($e->match, 30, 'correct response');

$e->send("quit\n");
