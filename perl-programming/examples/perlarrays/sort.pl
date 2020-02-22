#!/usr/bin/perl
use strict;
use warnings;

my @words = qw(Foo Moo Bar);

my @sorted_words = sort @words;
print "@sorted_words\n";  # Bar Foo Moo

my @data = (11, 2, 23, 12);
my @sorted = sort @data;
print "@sorted\n";         # 11 12 2 23

my @sorted_ascii = sort {$a cmp $b} @data;

my @sorted_numeric = sort {$a <=> $b} @data;
print "@sorted_numeric\n";  # 2 11 12 23

my @sorted_by_length
    = sort {length($a) <=> length($b)} @data;

my @sorted_by_length_and_ascii
    = sort {
               length($a) <=> length($b)
                       or
               $a cmp $b
           } @data;

my @sorted_by_abc = sort {lc($a) cmp lc($b)} @data;

my @sorted_abc_ascii
    = sort {
           lc($a) cmp lc($b)
                   or
               $a cmp $b
           } @data;
