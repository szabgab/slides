#!/usr/bin/perl -T
use strict;
use warnings;

use File::Spec;
use File::Basename;
use lib File::Spec->catfile(
            File::Basename::dirname(File::Spec->rel2abs($0)),
            '..',
            'lib');
BEGIN {
    print "$INC[0]\n";
}

