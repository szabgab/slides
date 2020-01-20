#!/usr/bin/perl
use strict;
use warnings;

use Expect;

my $e = Expect->new;
#$e->raw_pty(1);

$e->spawn("bc") or die "Cannot run bc\n";

$e->expect(1, -re => "warranty'\.") or die "no warranty\n";

$e->send("23+7\n");
$e->expect(1, -re => '\d+\+\d+') or die "no echo\n";
print $e->match, "\n";

$e->expect(1, -re => '\d+') or die "no sum\n";
my $match = $e->match;

if ($match eq "30") {
    print "Success\n";
} else {
    print "Failure. Received $match\n";
}

$e->send("quit\n");


