use strict;
use warnings;

use HTTP::CookieJar::LWP ();
use LWP::UserAgent       ();

use Test::More;

subtest first => sub {
    my $jar = HTTP::CookieJar::LWP->new;
    my $ua  = LWP::UserAgent->new(
        cookie_jar        => $jar,
        protocols_allowed => ['http', 'https'],
        timeout           => 10,
    );
    my $response = $ua->get('https://google.com/');
    ok $response->is_success;
    diag $jar->dump_cookies;
};

subtest second => sub {
    my $jar = HTTP::CookieJar::LWP->new;
    my $ua  = LWP::UserAgent->new(
        cookie_jar        => $jar,
        protocols_allowed => ['http', 'https'],
        timeout           => 10,
    );
    my $response = $ua->get('https://google.com/');
    ok $response->is_success;
    diag $jar->dump_cookies;
};



done_testing;
