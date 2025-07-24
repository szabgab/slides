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
    is $res->content, 'Get random <a href="/red">redirect</a>';
};

subtest redirect => sub {
    for (1..10) {
        my $res = $test->request(GET '/red');
        is $res->status_line, '302 Found', 'Status';
        ok exists $res->headers->{location};
        diag $res->headers->{location}
    }
};


done_testing();
