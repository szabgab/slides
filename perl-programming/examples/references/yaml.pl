#!/usr/bin/perl
use strict;
use warnings;

use YAML qw(DumpFile LoadFile);

my $data;
my $yml_file = 'data.yml';
if (-e $yml_file) {
    $data = LoadFile($yml_file);
} else {
    $data = {
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
}


print "Foo: $data->{people}{Foo}{phone}\n";       # Foo: 123
print "Bar: $data->{people}{Bar}{phones}->[0]\n"; # Bar: 345
print "Baz: $data->{people}{Baz}\n";              # Baz: NA

DumpFile $yml_file, $data;
