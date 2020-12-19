use strict;
use warnings;

use Test::More;
use Plack::Test;
use Plack::Util;
use HTTP::Request::Common;
use JSON::MaybeXS qw(decode_json);
use File::Temp qw(tempdir);
use File::Spec;

my $tmpdir = tempdir( CLEANUP => 1 );
$ENV{TODO_DB} = File::Spec->catfile($tmpdir, 'todo.json');

my $app = Plack::Util::load_psgi './app.psgi';

subtest main => sub {
    my $test = Plack::Test->create($app);
    my $res = $test->request(GET '/');

    is $res->status_line, '200 OK', 'Status';
    is $res->content, 'TODO', 'content of HTML page';
};


subtest various => sub {
    my $test = Plack::Test->create($app);

    my $res_add = $test->request(GET '/api/add/First item');
    is $res_add->status_line, '200 OK', 'Status';
    diag $res_add->content;
    my $resp_add = decode_json($res_add->content);
    is $resp_add->{status}, "ok", 'status field exists';
    like $resp_add->{elapsed}, qr{^\d+\.\d+$}, 'elapsed field looks good';
    my $id = $resp_add->{id};
    like $id, qr{^\d{8,}$}, 'id looks good';
    diag $id;
};


done_testing();
