use 5.010;
use strict;
use warnings;

use WWW::Mechanize;

my ($url) = @ARGV;
die "Usage: $0 URL\n" if not $url;

my $w = WWW::Mechanize->new;

$w->get($url);
say $w->content;

