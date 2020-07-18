#!/usr/bin/perl
use strict;
use warnings;

my $w;

if ($^O eq 'MSWin32') {
    require Win32::IE::Mechanize;
    $w = Win32::IE::Mechanize->new( visible => 1 );
} else {
    require WWW::Mechanize;
    $w = WWW::Mechanize->new();
}


my $url = "http://local/";
$w->get( $url );
$w->follow_link(text => "RecentChanges");
$w->follow_link(text => "AutoEditBox");

$w->submit_form(
    form_number => 2,
    button      => 'button-edit',
);
#print join "\n", $w->forms;
#foreach my $form ($w->forms) {
   
#}

$w->form_number(2);
my $wiki_text = $w->field('wiki_text');  # resets the field !
print "Content:\n$wiki_text\n"; 
$w->field('wiki_text', $wiki_text ."\nItt jart Matyas\n");
$w->click('button-save');


