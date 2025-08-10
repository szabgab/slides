del '/api/v2/item/:id' => sub {
    my $id = param('id');

    my $items = _mongodb('items');
    $items->remove({ _id => MongoDB::OID->new($id) });

    my $json = JSON::MaybeXS->new;
    return to_json { ok  => 1 };
};
