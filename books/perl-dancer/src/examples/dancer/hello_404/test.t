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
    is $res->content, 'Hello World!', 'Content';
};

subtest not_found => sub {
    my $res = $test->request(GET '/first');
    is $res->status_line, '404 Not Found', 'Status';
    like $res->content, qr{<title>Error 404 - Not Found</title>};
    like $res->content, qr{Powered by <a href="http://perldancer.org/">Dancer2</a>};
};

done_testing();
