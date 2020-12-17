use strict;
use warnings;

use Test::More;
use Plack::Test;
use Plack::Util;
use HTTP::Request::Common;
use HTTP::Cookies;

my $app = Plack::Util::load_psgi './app.psgi';

my $web = Plack::Test->create($app);
my $jar  = HTTP::Cookies->new;
my $base = 'http://localhost/';

subtest count => sub {
    my $res = $web->request(GET $base);
    is $res->status_line, '200 OK', 'Status';
    is $res->content, '1';
    $jar->extract_cookies($res);
};

subtest count2 => sub {
    my $req = GET $base;
    $jar->add_cookie_header($req);

    my $res = $web->request($req);
    is $res->content, '2';
};


done_testing();
