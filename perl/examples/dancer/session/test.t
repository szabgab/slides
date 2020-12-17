use strict;
use warnings;

use Test::More;
use Plack::Test;
use Plack::Util;
use HTTP::Request::Common;

my $app = Plack::Util::load_psgi './app.psgi';

my $web = Plack::Test->create($app);

subtest count => sub {
    my $res = $web->request(GET '/');
    is $res->status_line, '200 OK', 'Status';
    is $res->content, '1';

    TODO: {
        local $TODO = 'Send cookie or it starts counting from 1 again';
        $res = $web->request(GET '/');
        is $res->content, '2';
    }

    my $cookie = $res->headers->{'set-cookie'};
    diag $cookie;
};


done_testing();
