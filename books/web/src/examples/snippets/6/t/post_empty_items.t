my $res2  = $test->request( POST '/api/v2/item', { text => '' } );
is $res2->content, '{"error":"No text provided"}';

my $res3  = $test->request( POST '/api/v2/item' );
is $res3->content, '{"error":"No text provided"}';
