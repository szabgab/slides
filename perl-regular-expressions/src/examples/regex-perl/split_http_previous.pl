#!/usr/bin/perl
use strict;
use warnings;

use Data::Dumper;

my @input = (
    'fname=Foo&lname=Bar&email=foo@bar.com',
    'ip=127.0.0.1&machine=foobar',
);

foreach my $str (@input) {
    process($str);
}

sub process {
    my $str = shift;

    my @pairs = split /&/, $str;
    my %data;
    foreach my $p (@pairs) {
        my ($k, $v) = split /=/, $p;
        $data{$k} = $v;
    }
    print Dumper \%data;
}

