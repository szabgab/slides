use strict;
use warnings;

use Test::More;
use Plack::Test;
use HTTP::Request::Common;

my $app = do './app.psgi';

my $test = Plack::Test->create($app);

subtest main => sub {
    my $res = $test->request(GET '/');

    is $res->status_line, '200 OK', 'Status';
    is $res->content, '<a href="/user/1">One</a> <a href="/user/2">Two</a>';
};

subtest one => sub {
    my $res = $test->request(GET '/user/1');

    is $res->status_line, '200 OK', 'Status';
    is $res->content, '1', 'Content';
};

subtest anything => sub {
    my $res = $test->request(GET '/user/anything');

    is $res->status_line, '404 Not Found', 'Status';
    like $res->content, qr{<title>Error 404 - Not Found</title>};
    like $res->content, qr{Powered by <a href="http://perldancer.org/">Dancer2</a>};
};

subtest minus_one => sub {
    my $res = $test->request(GET '/user/-1');

    is $res->status_line, '200 OK', 'Status';
    is $res->content, '-1', 'Content';
};


done_testing();
