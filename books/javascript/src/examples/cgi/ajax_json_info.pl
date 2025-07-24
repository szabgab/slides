#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use JSON;


my $q = CGI->new;
print $q->header;
my $id = $q->param('id');

my @data = (
    {},
    {
        nickname => "Good",
        fname    => "Clint",
        lname    => "Eastwood",
    },
    {
        nickname => "Bad",
        fname    => "Lee",
        lname    => "Van Cleef",
    },
    {
        nickname => "Ugly",
        fname    => "Eli",
        lname    => "Wallach",
    },
);

# TODO check if id was supplied , is a numbr and is in the range
#
my $json = JSON->new;
print $json->objToJson($data[$id]);


