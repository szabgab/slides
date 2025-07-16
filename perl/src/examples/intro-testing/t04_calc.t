#!/usr/bin/perl
use strict;
use warnings;

use FindBin;
my $calc = "$FindBin::Bin/mycalc";

ok(`$calc 1  + 1` == 2);
ok(`$calc 2 + 2` == 4);
ok(`$calc 2 + 2 + 2` == 6);

sub ok {
    my ($ok) = @_;
    print $ok ? "ok\n" : "not ok\n";
}
