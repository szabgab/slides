#!/usr/bin/perl
use strict;
use warnings;

my $data_structure;
my $filename = 'dumped.data';
if (open my $fh, '<', $filename) {
    local $/ = undef;
    my $dump = <$fh>;
    eval $dump;
} else {
    die "Could not open '$filename' $!";
}

print "Foo: $data_structure->{phones}{Foo}\n"; # Foo: 123
print "Bar: $data_structure->{phones}{Bar}\n"; # Bar: 345
print "Baz: $data_structure->{phones}{Baz}\n"; # Baz: 678

