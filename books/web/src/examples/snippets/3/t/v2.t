subtest v2_reverse => sub {
    plan tests => 6;

    my $app = D2::Ajax->to_app;

    my $test = Plack::Test->create($app);
    my $res  = $test->request( GET '/api/v2/reverse?str=Hello world' );

    ok $res->is_success, '[GET /] successful';
    is $res->content, '{"text":"dlrow olleH"}';
    is $res->header('Content-Type'), 'application/json';
    is $res->header('Access-Control-Allow-Origin'), '*';

    my $res2  = $test->request( GET '/api/v2/reverse?str=' );
    is $res2->content, '{"text":""}';

    my $res3  = $test->request( GET '/api/v2/reverse' );
    is $res3->content, '{"text":""}';
};
