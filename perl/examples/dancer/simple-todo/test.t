use strict;
use warnings;

use Test::More;
use Test::Deep;
use Plack::Test;
use Plack::Util;
use HTTP::Request::Common;
use JSON::MaybeXS qw(decode_json encode_json);
use File::Temp qw(tempdir);
use Path::Tiny qw(path);
use Storable qw(dclone);

my $tmpdir = tempdir( CLEANUP => 1 );
my $db_file = path($tmpdir)->child('todo.json');
$ENV{TODO_DB} = $db_file;
my $ELAPSED = qr{^\d+\.\d+$};

my %data = (
    "123" => "Hello world",
    "124" => "Something else",
    "738" => "A 3rd row",
);


my $app = Plack::Util::load_psgi './app.psgi';

subtest main => sub {
    my $test = Plack::Test->create($app);
    my $res = $test->request(GET '/');

    is $res->status_line, '200 OK', 'Status';
    is $res->content, 'TODO', 'content of HTML page';
};



subtest add_first => sub {
    my $test = Plack::Test->create($app);

    unlink $db_file if -e $db_file;

    my $text = 'First item';
    my $res_add = $test->request(GET "/api/add/$text");
    is $res_add->status_line, '200 OK', 'Status';
    diag $res_add->content;
    my $resp_add = decode_json($res_add->content);
    is $resp_add->{status}, "ok", 'status field exists';
    like $resp_add->{elapsed}, $ELAPSED, 'elapsed field looks good';
    my $id = $resp_add->{id};
    like $id, qr{^\d{8,}$}, 'id looks good';
    diag $id;

    my $json = decode_json(path($db_file)->slurp);
    is_deeply $json, { $id => $text };
};

subtest add_more => sub {
    my $test = Plack::Test->create($app);

    path($db_file)->spew(encode_json(\%data));

    my $text = 'Another item';
    my $res_add = $test->request(GET "/api/add/$text");
    is $res_add->status_line, '200 OK', 'Status';
    diag $res_add->content;
    my $resp_add = decode_json($res_add->content);
    is $resp_add->{status}, "ok", 'status field exists';
    like $resp_add->{elapsed}, $ELAPSED, 'elapsed field looks good';
    my $id = $resp_add->{id};
    like $id, qr{^\d{8,}$}, 'id looks good';
    diag $id;

    my $json = decode_json(path($db_file)->slurp);
    is_deeply $json, { %data, $id => $text };
};


subtest good_get => sub {
    my $test = Plack::Test->create($app);

    path($db_file)->spew(encode_json(\%data));

    my $id = '123';

    my $res_add = $test->request(GET "/api/get/$id");
    is $res_add->status_line, '200 OK', 'Status';
    diag $res_add->content;
    my $resp = decode_json($res_add->content);
    like $resp->{elapsed}, $ELAPSED, 'elapsed';
    delete $resp->{elapsed};
    is_deeply $resp, { "status" => "ok", text => $data{$id}, id => $id }, 'returned json data';

    my $json = decode_json(path($db_file)->slurp);
    is_deeply $json, \%data;
};

subtest bad_get => sub {
    my $test = Plack::Test->create($app);

    path($db_file)->spew(encode_json(\%data));

    my $id = '42';

    my $res_add = $test->request(GET "/api/get/$id");
    is $res_add->status_line, '404 Not Found', 'Status';
    diag $res_add->content;
    my $resp = decode_json($res_add->content);
    like $resp->{elapsed}, $ELAPSED, 'elapsed';
    delete $resp->{elapsed};
    is_deeply $resp, { "status" => "failure", id => $id }, 'returned json data';

    my $json = decode_json(path($db_file)->slurp);
    is_deeply $json, \%data;
};

subtest good_del => sub {
    my $test = Plack::Test->create($app);

    path($db_file)->spew(encode_json(\%data));

    my $id = '123';

    my $res_add = $test->request(GET "/api/del/$id");
    is $res_add->status_line, '200 OK', 'Status';
    diag $res_add->content;
    my $resp = decode_json($res_add->content);
    like $resp->{elapsed}, $ELAPSED, 'elapsed';
    delete $resp->{elapsed};
    is_deeply $resp, { "status" => "ok", id => $id, text => $data{$id} }, 'returned json data';

    my $json = decode_json(path($db_file)->slurp);
    my $reduced_data = dclone \%data;
    delete $reduced_data->{$id};
    is_deeply $json, $reduced_data;
};



subtest bad_del => sub {
    my $test = Plack::Test->create($app);

    path($db_file)->spew(encode_json(\%data));

    my $id = '42';

    my $res_add = $test->request(GET "/api/del/$id");
    is $res_add->status_line, '404 Not Found', 'Status';
    diag $res_add->content;
    my $resp = decode_json($res_add->content);
    like $resp->{elapsed}, $ELAPSED, 'elapsed';
    delete $resp->{elapsed};
    is_deeply $resp, { "status" => "failure", id => $id }, 'returned json data';

    my $json = decode_json(path($db_file)->slurp);
    is_deeply $json, \%data;
};


subtest list => sub {
    my $test = Plack::Test->create($app);

    my @items = map { { id => $_, text => $data{$_} } }  keys %data;

    path($db_file)->spew(encode_json(\%data));

    my $res_add = $test->request(GET '/api/list');
    is $res_add->status_line, '200 OK', 'Status';
    diag $res_add->content;
    my $resp = decode_json($res_add->content);
    like $resp->{elapsed}, $ELAPSED, 'elapsed';
    delete $resp->{elapsed};
    cmp_deeply $resp, { "status" => "ok", items => bag @items }, 'returned json data';

    my $json = decode_json(path($db_file)->slurp);
    is_deeply $json, \%data;
};


done_testing();
