use MongoDB ();

post '/api/v2/item' => sub {
    my $text = param('text') // '';
    $text =~ s/^\s+|\s+$//g;
    if ($text eq '') {
        return to_json { error => 'No text provided' };
    }

    my $client = MongoDB::MongoClient->new(host => 'localhost', port => 27017);
    my $db   = $client->get_database( 'd2-ajax' );
    my $items = $db->get_collection('items');
    $items->insert({
        text => $text,
    });
    return to_json { ok => 1, text => $text };
};
