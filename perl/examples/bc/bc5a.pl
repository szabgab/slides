#!/usr/bin/perl
use strict;
use warnings;

use FindBin;

use Expect;
use Test::More;

$Expect::Log_Stdout = 0;

my @sets = read_file();

plan tests => 2 * scalar @sets;

my $e = Expect->new;
$e->raw_pty(1);
$e->spawn("bc") or die "Could not start bc\n";
$e->expect(1, [qr/warranty'./]) or die "no warranty\n";

foreach my $set (@sets) {
    $e->send("$set->[0]\n");
    ok($e->expect(1, [qr/\d+/]), 'numbers received');
    is($e->match, $set->[1], "expected value of " . $set->[0]);
}


$e->send("quit\n");


sub read_file {
    open my $fh, "<", "$FindBin::Bin/bc_input.txt"
         or die "Could not open bc_input.txt";

    my @data;
    while (my $line = <$fh>) {
        chomp $line;
        push @data, [split /\s*,\s*/, $line];
    }
    return @data;
}

