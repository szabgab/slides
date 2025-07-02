use strict;
use warnings;

use Test::More;
use Plack::Test;
use Plack::Util;
use HTTP::Request::Common;

my $app = Plack::Util::load_psgi './app.psgi';

my $test = Plack::Test->create($app);

subtest one => sub {
    my $res = $test->request(GET '/user/1');

    is $res->status_line, '200 OK', 'Status';
    is $res->content, '1', 'Content';
};

subtest minus_one => sub {
    my $res = $test->request(GET '/user/-1');

    is $res->status_line, '404 Not Found', 'Status';
    is $res->content, 'No such ID', 'Content';
};

subtest no42 => sub {
    my $res = $test->request(GET '/user/42');

    is $res->status_line, '404 Not Found', 'Status';
    is $res->content, 'No such ID', 'Content';
};


done_testing();
