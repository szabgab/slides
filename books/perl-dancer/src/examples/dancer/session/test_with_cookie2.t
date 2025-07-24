use strict;
use warnings;

use Test::More;
use Plack::Test;
use Plack::Util;
use HTTP::Request::Common;
use HTTP::Cookies;

my $app1 = Plack::Util::load_psgi './app.psgi';
my $web1 = Plack::Test->create($app1);
my $jar1  = HTTP::Cookies->new;

my $app2 = Plack::Util::load_psgi './app.psgi';
my $web2 = Plack::Test->create($app2);
my $jar2  = HTTP::Cookies->new;

my $base = 'http://localhost/';

subtest count1_1 => sub {
    my $res = $web1->request(GET $base);
    is $res->status_line, '200 OK', 'Status';
    is $res->content, '1';
    $jar1->extract_cookies($res);
};

subtest count1_2 => sub {
    my $req = GET $base;
    $jar1->add_cookie_header($req);

    my $res = $web1->request($req);
    is $res->content, '2';
};

subtest count1_3 => sub {
    my $req = GET $base;
    $jar1->add_cookie_header($req);

    my $res = $web1->request($req);
    is $res->content, '3';
};

subtest count2_1 => sub {
    my $res = $web2->request(GET $base);
    is $res->status_line, '200 OK', 'Status';
    is $res->content, '1';
    $jar2->extract_cookies($res);
};

subtest count1_4 => sub {
    my $req = GET $base;
    $jar1->add_cookie_header($req);

    my $res = $web1->request($req);
    is $res->content, '4';
};


subtest count2_2 => sub {
    my $req = GET $base;
    $jar2->add_cookie_header($req);

    my $res = $web2->request($req);
    is $res->content, '2';
};




done_testing();
