#!/usr/bin/perl
use strict;
use warnings;

use YAML qw(DumpFile);

my $data_structure = {
    people => {
        Foo     => {
                phone => '123',
        },
        Bar     => {
            phones => [
                    '345',
                    '678',
            ],
            title => 'CEO',
        },
        Baz     => 'NA',
    }
};

DumpFile 'data.yml', $data_structure;

