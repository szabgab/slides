sub _mongodb {
    my ($collection) = @_;

    my $client = MongoDB::MongoClient->new(host => 'localhost', port => 27017);
    my $db   = $client->get_database( config->{app}{mongodb} );
    return $db->get_collection($collection);
}
