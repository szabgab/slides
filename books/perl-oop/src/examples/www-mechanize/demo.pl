use strict;
use warnings;
use feature 'say';
our $VERSION = '0.01';

use WWW::Mechanize;

my $url = shift @ARGV or die "Usage $0 URL";
# say $WWW::Mechanize::VERSION;


my $mech = WWW::Mechanize->new(autocheck => 0);
my $res = $mech->get($url);
say $res->status_line;
say $mech->status();
say $mech->res->status_line;

say '';

$mech->dump_headers();
say '';

if ($mech->success) {
    print $mech->content;
}
