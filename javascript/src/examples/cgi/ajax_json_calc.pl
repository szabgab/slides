#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use JSON;


my $q = CGI->new;
print $q->header;
my $str = $q->param('str');

# TODO check if id was supplied , is a numbr and is in the range
#
my $json = JSON->new;
my $data = $json->jsonToObj($str);
my %ops = map {$_ => 1} qw(+ - * /);
use Data::Dumper;
warn $str;
warn Dumper $data;

my %response = (
    input => "$data->{x} $data->{op} $data->{y}",
);

if ($data->{x} =~ /^\d+$/ and
   $ops{ $data->{op} } and
   $data->{y}  =~ /^\d+$/) {

   $response{result} = eval $response{input};
} else {
    $response{error} = "Invalid input";
}

print $json->objToJson(\%response);



