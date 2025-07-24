#!/usr/bin/perl
use strict;
use warnings;

sub fix_date {
    my $str = shift;
    $str =~ s/-(\d)\b/-0$1/g;
    return $str;
}


my %dates = (
    '2010-7-5'   => '2010-07-05',
    '2010-07-5'  => '2010-07-05',
    '2010-07-05' => '2010-07-05',
    '2010-7-15'  => '2010-07-15',
);

use Test::More;
plan tests => scalar keys %dates;

foreach my $in (sort keys %dates) {
    my $result = fix_date($in);

    is $result, $dates{$in}, $in;

#    print  "      old: $in\n";
#    print  "      new: $result\n";
#    print  " expected: $dates{$in}\n\n";
}

