use strict;
use warnings;

use Test::More;
use Plack::Test;
use Plack::Util;
use HTTP::Request::Common;
use JSON::MaybeXS qw(decode_json);

my $app = Plack::Util::load_psgi './app.psgi';

subtest main => sub {
    my $test = Plack::Test->create($app);
    my $res = $test->request(GET '/');

    is $res->status_line, '200 OK', 'Status';
    is $res->headers->{'content-type'}, 'text/html; charset=UTF-8';
};

subtest one => sub {
    my $test = Plack::Test->create($app);
    my $res = $test->request(GET '/api/1');

    is $res->status_line, '200 OK', 'Status';
    is_deeply decode_json($res->content), {
        name => 'Dancer',
        language => 'Perl',
    };
    is $res->headers->{'content-type'}, 'application/json';
};

subtest two => sub {
    my $test = Plack::Test->create($app);
    my $res = $test->request(GET '/api/2');

    is $res->status_line, '200 OK', 'Status';
    is_deeply decode_json($res->content), {
        name => 'Dancer2',
        language => 'Perl 7',
    };
    is $res->headers->{'content-type'}, 'application/json; charset=UTF-8';
};

subtest three => sub {
    my $test = Plack::Test->create($app);
    my $res = $test->request(GET '/api/3');

    is $res->status_line, '200 OK', 'Status';
    is_deeply decode_json($res->content), {
        answer => '42',
    };
    is $res->headers->{'content-type'}, 'application/json';
};




done_testing();
