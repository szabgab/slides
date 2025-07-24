use strict;
use warnings;

use Mojo::UserAgent;

my $ua = Mojo::UserAgent->new;
print $ua->get('http://www.yapcna.org/yn2016/')
    ->res->dom->find('div[class=row h1]')->[0];

