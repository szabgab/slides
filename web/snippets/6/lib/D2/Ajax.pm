get '/api/v2/items' => sub {
    my $client = MongoDB::MongoClient->new(host => 'localhost', port => 27017);
    my $db   = $client->get_database( config->{app}{mongodb} );
    my $items = $db->get_collection('items');

    my @data =  $items->find->all;
    my $json = JSON::MaybeXS->new;
    $json->convert_blessed(1);
    return $json->encode( { items =>  \@data } );
};
