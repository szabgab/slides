use strict;
use warnings;

use Test::More;
use Plack::Test;
use Plack::Util;
use HTTP::Request::Common;
use File::Temp qw(tempdir);
use File::Spec;

my $tmpdir = tempdir( CLEANUP => 1 );
$ENV{COUNTER_FILE} = File::Spec->catfile($tmpdir, 'cnt.json');
diag $ENV{COUNTER_FILE};

my $app = Plack::Util::load_psgi './app.psgi';

my $test = Plack::Test->create($app);

subtest main_1 => sub {
    my $res = $test->request(GET '/');

    is $res->status_line, '200 OK', 'Status';
    like $res->content, qr{<h1>Counters</h1>}, 'title';
    unlike $res->content, qr{apple}, 'title';
    unlike $res->content, qr{peach}, 'title';
};

my @cases = (
    ['/apple' => '1'],
    ['/apple' => '2'],
    ['/apple' => '3'],
    ['/peach' => '1'],
    ['/apple' => '4'],
);

subtest count => sub {
    for my $case (@cases) {
        my $res = $test->request(GET $case->[0]);
        is $res->status_line, '200 OK', 'Status';
        is $res->content, $case->[1], 'one';
    }
};

subtest main_2 => sub {
    my $res = $test->request(GET '/');

    is $res->status_line, '200 OK', 'Status';
    like $res->content, qr{<h1>Counters</h1>}, 'title';
    like $res->content, qr{<li>apple: 4</li>}, 'title';
    like $res->content, qr{<li>peach: 1</li>}, 'title';
};


done_testing;

