my $options  = $test->request( OPTIONS '/api/v2/item/anything' );
ok $options->is_success, '[POST /] successful';
is $options->header('Access-Control-Allow-Methods'), 'GET, POST, OPTIONS, DELETE';
