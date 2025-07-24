#!/usr/bin/perl
use strict;
use warnings;

use Win32::IE::Mechanize;
my $w = Win32::IE::Mechanize->new( visible => 1 );


my $url = "http://local/";
$w->get( $url );
$w->follow_link(text => "RecentChanges");
$w->follow_link(text => "AutoEditBox");

$w->submit_form(
    form_number => 2,
    button      => 'button-edit',
);

$w->form_number(2);
my $wiki_text = $w->field('wiki_text');  # resets the field !
$w->field('wiki_text', $wiki_text ."\nItt jart Matyas\n");
$w->click('button-save');

