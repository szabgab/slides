use strict;
use warnings;

use Mojo::UserAgent;

use Data::Dumper qw(Dumper);

my $ua = Mojo::UserAgent->new;
print Dumper $ua->get('https://api.metacpan.org/v0/release/_search?q=status:latest&fields=name,status,date&sort=date:desc&size=10')
    ->res->json;

