use strict;
use warnings;

use FindBin;
use Test::More;

my @files = glob "$FindBin::Bin/[0-9]*.t";

plan tests => scalar @files;

my $T = Test::More->builder;

foreach my $file (@files) {
    if ($file =~ /explain/) {
        $T->skip("Not this one");
        next;
    }
    ok(-e $file, $file);
}

