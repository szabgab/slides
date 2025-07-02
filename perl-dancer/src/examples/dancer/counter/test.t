use strict;
use warnings;

use Test::More;
use Plack::Test;
use Plack::Util;
use HTTP::Request::Common;
use File::Temp qw(tempdir);
use File::Spec;

my $tmpdir = tempdir( CLEANUP => 1 );
$ENV{COUNTER_TEST_FILE} = File::Spec->catfile($tmpdir, 'cnt.txt');
diag $ENV{COUNTER_TEST_FILE};

my $app = Plack::Util::load_psgi './app.psgi';


subtest one => sub {
    my $test = Plack::Test->create($app);
    my $res = $test->request(GET '/');

    is $res->status_line, '200 OK', 'Status';
    is $res->content, '1', 'Content';
};

subtest two => sub {
    my $test = Plack::Test->create($app);
    my $res = $test->request(GET '/');

    is $res->status_line, '200 OK', 'Status';
    is $res->content, '2', 'Content';
};



done_testing;

