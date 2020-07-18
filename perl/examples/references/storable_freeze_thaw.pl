#!/usr/bin/perl
use strict;
use warnings;

use Storable qw(freeze thaw);

my $data_structure = {
    phones => {
        Foo     => 123, 
        Bar     => 345,
        Baz     => 678,
    }
};

my $frozen = freeze $data_structure;

# here send it over the network 
# or save it in a database

my $new_data_structure = thaw $frozen;

print "$new_data_structure->{phones}{Foo}\n"; # 123
print "$new_data_structure->{phones}{Bar}\n"; # 345

print "$data_structure\n";      # HASH(0x4e8144)
print "$new_data_structure\n";  # HASH(0x27b4a3c)

print "$data_structure->{phones}\n";     # HASH(0x4e7fe4)
print "$new_data_structure->{phones}\n"; # HASH(0x1ffe294)
