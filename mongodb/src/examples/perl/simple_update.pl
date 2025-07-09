use strict;
use warnings;
use 5.010;

use MongoDB ();
use Data::Dumper qw(Dumper);

my $client = MongoDB::MongoClient->new(host => 'localhost', port => 27017);
my $db   = $client->get_database( 'example_' . $$ . '_' . time  );

my $people_coll = $db->get_collection('people');

$people_coll->insert( {
    name => 'First',
});

$people_coll->insert( {
    name => 'Second',
});

$people_coll->update(
    { name => 'Second'},
    { '$set' => {
            phone => '1-123',
        },
    },
);

my $people = $people_coll->find;
while (my $p = $people->next) {
    print Dumper $p;
}

END {
    $db->drop if $db;
}


