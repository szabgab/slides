use strict;
use warnings;
use 5.010;

use WWW::Mechanize::PhantomJS;
my $mech = WWW::Mechanize::PhantomJS->new();
$mech->get('http://localhost:8080/');
say $mech->content;
