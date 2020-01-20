use strict;
use warnings;

use Test::More;
use WWW::Mechanize;

plan tests => 3;

my $url = 'http://www.yapcna.org/yn2013';
my $w = WWW::Mechanize->new;
$w->get("$url/login");
unlike $w->content, qr{logout};

#diag explain $w->cookie_jar;

#print $w->current_form->dump;

$w->submit_form(
  form_number => 1,
  fields => {
     'credential_0' => 'szabgab',
     'credential_1' =>  $ARGV[0],
  },
);
like $w->content, qr{logout};

my $other = WWW::Mechanize->new;
$other->get("$url/login");
unlike $other->content, qr{logout};


