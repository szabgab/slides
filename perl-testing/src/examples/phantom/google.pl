use strict;
use warnings;
use 5.010;

use WWW::Mechanize::PhantomJS;
my $mech = WWW::Mechanize::PhantomJS->new();
$mech->get('http://google.com');
say $mech->content;
