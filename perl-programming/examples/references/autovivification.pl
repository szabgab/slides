#!/usr/bin/perl
use strict;
use warnings;

use Data::Dumper;

my $data;
$data->{Foo}{Age} = 23;

print Dumper $data;

if ($data->{Bar}{Age} > 18) {
    print "Your are too old\n";
}

print Dumper $data;


delete $data->{Moo}{Age};

print Dumper $data;
