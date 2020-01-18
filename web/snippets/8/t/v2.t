my @items = ("One 1", "Two 2", "Three 3");
foreach my $it (@items) {
    my $res = $test->request( POST '/api/v2/item', { text => $it });
    is_deeply decode_json($res->content), { ok => 1, text => $it };
}
my $get5  = $test->request( GET '/api/v2/items');
my $items5 = decode_json($get5->content);
is scalar @{$items5->{items}}, 5;

my $del3  = $test->request( DELETE '/api/v2/item/' . $items5->{items}[3]{'_id'}{'$oid'} );
is $del3->content, '{"ok":1}';

my $get6  = $test->request( GET '/api/v2/items');
my $items6 = decode_json($get6->content);
is scalar @{$items6->{items}}, 4;
is_deeply $items5->{items}[0], $items6->{items}[0];
is_deeply $items5->{items}[1], $items6->{items}[1];
is_deeply $items5->{items}[2], $items6->{items}[2];
is_deeply $items5->{items}[4], $items6->{items}[3];
is_deeply $items5->{items}[5], $items6->{items}[4];
