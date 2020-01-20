#!/usr/bin/perl
use strict;
use warnings;

use JSON qw(from_json to_json);

my $data;
my $json_file = 'data.json';
if (-e $json_file) {
    open my $fh, '<', $json_file or die;
    local $/ = undef;
    my $json = <$fh>;
    $data = from_json($json);
} else {
    # initialize
    $data = {
        phones => {
            Foo     => 0,
            Bar     => 0,
            Baz     => 0,
        }
    };
}


# update data
$data->{phones}{Foo} += 1 * int rand 5;
$data->{phones}{Bar} += 3 * int rand 5;
$data->{phones}{Baz} += 9 * int rand 5;

print "Foo: $data->{phones}{Foo}\n";
print "Bar: $data->{phones}{Bar}\n";
print "Baz: $data->{phones}{Baz}\n";

open my $out, '>', $json_file or die;
print $out to_json($data, { pretty => 1, utf8 => 1, });
