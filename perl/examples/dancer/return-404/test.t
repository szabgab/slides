use strict;
use warnings;

use Test::More;
use Plack::Test;
use Plack::Util;
use HTTP::Request::Common;

my $app = Plack::Util::load_psgi './app.psgi';

my $test = Plack::Test->create($app);

subtest main => sub {
    my $res = $test->request(GET '/');

    is $res->status_line, '200 OK', 'Status';
    is $res->content, '<a href="/user/1">One</a> <a href="/user/2">Two</a>', 'Content';
};

subtest one => sub {
    my $res = $test->request(GET '/user/1');

    is $res->status_line, '200 OK', 'Status';
    is $res->content, '1', 'Content';
};

subtest two => sub {
    my $res = $test->request(GET '/user/2');

    is $res->status_line, '404 Not Found', 'Status';
    is $res->content, 'No such ID', 'Content';
};


done_testing();
