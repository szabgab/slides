use v5.36;

use Data::Dumper qw(Dumper);

use WWW::Mechanize;

my $url = shift @ARGV or die "Usage $0 URL";

my $mech = WWW::Mechanize->new(autocheck => 0);
say $mech;
say Dumper $mech;

