use JSON::MaybeXS qw(decode_json);

subtest v2_items => sub {
    plan tests => 4;

    my $app = D2::Ajax->to_app;

    my $test = Plack::Test->create($app);

    my $res  = $test->request( POST '/api/v2/item', {text => 'First Thing to do' } );
    ok $res->is_success, '[POST /] successful';
    is_deeply decode_json($res->content), { ok => 1, text  => 'First Thing to do' };
    is $res->header('Content-Type'), 'application/json';
    is $res->header('Access-Control-Allow-Origin'), '*';
};
