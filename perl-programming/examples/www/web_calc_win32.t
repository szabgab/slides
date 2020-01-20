#!/usr/bin/perl
use strict;
use warnings;

use Test::More qw(no_plan);
use Win32::IE::Mechanize;

my $url = 'http://localhost/calculator.html';
my $w = Win32::IE::Mechanize->new( visible => 1 );
$w->get($url);

is($w->status, 200, 'fetched ok');

like($w->content, qr{Calculator}, 'start page ok');

my @f = $w->forms;
is (@f, 1, 'there is one form on this page');

# shall I check if all the parts of the form are there ???

$w->submit_form(
    fields => {
        a => 23,
        b => 19,
    },
);
like($w->content, qr{<h1 align="center">42</h1>}, 'get 42');

$w->back;

my @comps = (
    [23, 19, 42],
    [1,   2,  3],
    [1,   -1, 2],
);

foreach my $c (@comps) {
    $w->submit_form(
        fields => {
            a => $$c[0],
            b => $$c[1],
        },
    );
    like($w->content, qr{<h1 align="center">$$c[2]</h1>}, "$$c[0]+$$c[1]=$$c[2]");

    $w->back;
}

