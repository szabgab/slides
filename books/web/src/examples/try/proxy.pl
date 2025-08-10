use strict;
use warnings;

use Dancer2;
use LWP::UserAgent;
use HTTP::Request;
use URI::Escape qw(uri_unescape);

get '/' => sub {
    return q{<form method="POST"> <input name="q"><input type="submit" value="Send"></form>};
};

post '/' => sub {
    my $raw_url = substr request->{body}, 2;
    my $ua = LWP::UserAgent->new;
    debug $raw_url;
    my $url = uri_unescape $raw_url;
    debug $url;
    my $request = HTTP::Request->new(GET => $url);
    my $response = $ua->request($request);
    return $response->content;
};

dance;

