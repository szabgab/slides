#!/usr/bin/perl
use strict;
use warnings;

use Test::More tests => 14;
use WWW::Mechanize;
#use Test::HTML::Tidy;

my $SERVER = 'http://localhost:8080';

my $url  = $SERVER;

my $mech = WWW::Mechanize->new;
$mech->get($url);
is   $mech->status, 200, 'main page fetched';
like $mech->content, qr{Our languages}, 'content';

$mech->follow_link( text => 'calculator' );
is   $mech->status, 200, 'calculator page fetched';
like $mech->content, qr{Calculator}, 'start page ok';

#html_tidy_ok $mech->content, "html is tidy";

my @forms = $mech->forms;
is @forms, 1, 'there is one form on this page';



# Shall we check if all the parts of the form are there? 
is $forms[0]->action, "$SERVER/cgi/cgi_sum.pl", "action URL is correct";
my @inputs = $forms[0]->inputs;
is @inputs, 3, "there are 3 input fields on this form";
{
    my $a = $forms[0]->find_input('a');
    isa_ok $a, 'HTML::Form::TextInput';

    my $b = $forms[0]->find_input('b');
    isa_ok $b, 'HTML::Form::TextInput';

    my $s = $forms[0]->find_input('submit');
    isa_ok $s, 'HTML::Form::SubmitInput';
}

# Shall we check the name of the form ?


$mech->submit_form(
    fields => {
       a => 23,
       b => 19,
    },
);
like $mech->content, qr{<h1 align="center">42</h1>}, 'get 42';

#html_tidy_ok $mech->content, "result html is tidy";
$mech->back;

my @comps = (
   [23, 19, 42],
   [1,   2,  3],
   [1,   -1, 0],
);

foreach my $c (@comps) {
   $mech->submit_form(
      fields => {
       a => $c->[0],
       b => $c->[1],
      },
   );
   like $mech->content, 
        qr{<h1 align="center">$c->[2]</h1>},
        "$c->[0]+$c->[1]=$c->[2]";

   $mech->back;
}

