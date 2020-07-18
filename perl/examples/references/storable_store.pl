#!/usr/bin/perl
use strict;
use warnings;

use Storable qw(store);

my $data_structure = {
    phones => {
        Foo     => 123, 
        Bar     => 345,
        Baz     => 678,
    }
};

store $data_structure, 'frozen.data' or die;

