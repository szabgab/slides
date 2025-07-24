#!/usr/bin/perl
use strict;
use warnings;

use Data::Dumper ();

my $data_structure = {
    phones => {
        Foo     => 123, 
        Bar     => 345,
        Baz     => 678,
    }
};

open my $fh, '>', 'dumped.data' or die;
print $fh Data::Dumper->Dump([$data_structure], ['data_structure']);
close $fh;

