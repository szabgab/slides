#!/usr/bin/perl
use strict;
use warnings;

my $filename = "some_filename";
open(my $fhb, "<",  $filename);          # read
open(my $fhc, ">",  $filename);          # write
open(my $fhd, ">>", $filename);          # append
open(my $fhe, "+<", $filename);          # read and write
