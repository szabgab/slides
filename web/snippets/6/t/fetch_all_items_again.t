my $get3  = $test->request( GET '/api/v2/items');
my $items3 = decode_json($get3->content);
is scalar @{$items3->{items}}, 1;
is $items3->{items}[0]{text}, 'First Thing to do';
