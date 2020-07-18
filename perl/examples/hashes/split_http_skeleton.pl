#!/usr/bin/perl
use strict;
use warnings;
use Data::Dumper qw(Dumper);
 
my @input = (
    'fname=Foo&lname=Bar&email=foo@bar.com',
    'ip=127.0.0.1&machine=foobar',
);

foreach my $str (@input) {
    process($str);
}

sub process {

    my %data;

    # put your code here

    print Dumper \%data;
}
