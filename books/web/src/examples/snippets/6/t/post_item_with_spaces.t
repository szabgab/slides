my $res4  = $test->request( POST '/api/v2/item', { text => '  one more  ' });
is_deeply decode_json($res4->content), { ok => 1, text => 'one more' };

my $get4  = $test->request( GET '/api/v2/items');
my $items4 = decode_json($get4->content);
is scalar @{$items4->{items}}, 2;
is $items4->{items}[0]{text}, 'First Thing to do';
is $items4->{items}[1]{text}, 'one more';
