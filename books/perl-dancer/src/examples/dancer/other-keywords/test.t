use strict;
use warnings;

use Test::More;
use Plack::Test;
use Plack::Util;
use HTTP::Request::Common qw(GET PUT DELETE PATCH OPTIONS);

my $app = Plack::Util::load_psgi './app.psgi';

my $test = Plack::Test->create($app);

subtest main => sub {
    my $res = $test->request(GET '/');

    is $res->status_line, '200 OK', 'Status';
    like $res->content, qr{Try PUT /myput}, 'Content';
};

subtest myput => sub {
    my $res = $test->request(PUT '/myput', { message => 'Foo Bar' });

    is $res->status_line, '200 OK', 'Status';
    is $res->content, 'got PUT with Foo Bar', 'Content';
};

subtest mydel => sub {
    my $res = $test->request(DELETE '/mydel?message=Foo Bar');

    is $res->status_line, '200 OK', 'Status';
    is $res->content, 'got DELETE with Foo Bar', 'Content';
};

subtest mypatch => sub {
    my $res = $test->request(PATCH '/mypatch', { message => 'Foo Bar' });

    is $res->status_line, '200 OK', 'Status';
    is $res->content, 'got PATCH with Foo Bar', 'Content';
};

subtest myoptions => sub {
    my $res = $test->request(OPTIONS '/myoptions', { message => 'Foo Bar' });

    is $res->status_line, '200 OK', 'Status';
    is $res->content, 'got OPTIONS with Foo Bar', 'Content';
};



done_testing();
