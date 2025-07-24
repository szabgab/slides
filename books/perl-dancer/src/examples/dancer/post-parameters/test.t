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
    like $res->content, qr{<form action="/echo" method="POST">}, 'Content';
};

subtest echo => sub {
    my $res = $test->request(POST '/echo', { message => 'Foo Bar' });

    is $res->status_line, '200 OK', 'Status';
    is $res->content, 'You typed in Foo Bar', 'Content';
};


done_testing();
