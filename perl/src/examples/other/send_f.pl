use strict;
use warnings;

use LWP::UserAgent ();
use HTTP::Request::Common qw(POST);

my $ua = LWP::UserAgent->new(timeout => 10);
my $url = 'https://httpbin.org/post';
my %content = (
    field => 'value',
    name => 'Corion',
);

my $request = POST $url, 'Content-Type' => 'form-data', Content => \%content;
my $response = $ua->request($request);
print $response->decoded_content;
