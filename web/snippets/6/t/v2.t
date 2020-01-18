my $get1  = $test->request( GET '/api/v2/items');
my $items1 = decode_json($get1->content);
is scalar @{$items1->{items}}, 1;
is $items1->{items}[0]{text}, 'First Thing to do';
