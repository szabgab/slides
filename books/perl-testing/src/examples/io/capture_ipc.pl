#!/usr/bin/perl
use strict;
use warnings;

use Test::More tests => 2;
use IPC::Run3;

my $app = "./examples/io/application.pl";

my @in = ('10', '21', 'hello', '3x');
my $in = join "\n", @in;

my @expected_out = ('20', '42');
my @expected_err = (
        "The input 'hello' contains no numeric values", 
        "The input '3x' contains no numeric values",
    );

{
    my $out;
    my $err;
    run3 [$app], \$in, \$out, \$err;

    my $expected_out = join("\n", @expected_out) . "\n";
    is($out, $expected_out, "IPC Output");
    my $expected_err = join("\n", @expected_err) . "\n";
    is($err, $expected_err, "IPC Error");
}

