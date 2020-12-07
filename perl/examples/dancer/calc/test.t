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
    like $res->content, qr{<form action="/calc" method="POST">}, 'Content';
};

subtest calc => sub {
    my @cases = (
        [{ x => '10', y => '2', op => 'add'}, '12'],
        [{ x => '10', y => '2', op => 'multiply'}, '20'],
        [{ x => '10', y => '2', op => 'deduct'}, '8'],
        [{ x => '10', y => '2', op => 'div'}, '5'],
    );

    for my $case (@cases) {
        my $res = $test->request(POST '/calc', $case->[0]);
        is $res->status_line, '200 OK', 'Status';
        is $res->content, "The result is $case->[1]", 'Content';
    }
};


done_testing();
