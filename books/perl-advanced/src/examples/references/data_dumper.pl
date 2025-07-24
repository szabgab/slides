#!/usr/bin/perl
use strict;
use warnings;

use Data::Dumper ();

my $data_structure;
my $filename = 'dumped.data';

if (-e $filename and open my $fh, '<', $filename) {
    local $/ = undef;
    my $dump = <$fh>;
    eval $dump;
} else {
    # initialize
    $data_structure = {
        phones => {
            Foo     => 0, 
            Bar     => 0,
            Baz     => 0,
        }
    }
};

# update data
$data_structure->{phones}{Foo} += 1 * int rand 5;
$data_structure->{phones}{Bar} += 3 * int rand 5;
$data_structure->{phones}{Baz} += 9 * int rand 5;


print "Foo: $data_structure->{phones}{Foo}\n";
print "Bar: $data_structure->{phones}{Bar}\n";
print "Baz: $data_structure->{phones}{Baz}\n";


open my $fh, '>', $filename or die;
print $fh Data::Dumper->Dump([$data_structure], ['data_structure']);
close $fh;
