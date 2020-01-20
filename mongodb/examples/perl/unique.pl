use strict;
use warnings;
use 5.010;

use MongoDB ();
use Data::Dumper qw(Dumper);

my $client = MongoDB::MongoClient->new(host => 'localhost', port => 27017);
my $db   = $client->get_database( 'training' );
$db->drop;
#my @collections = $db->collection_names;


# without sparse we can get one document without the indexed field
# with spars=true we can get more such documents
my $users_coll = $db->get_collection('users');
my $res = $users_coll->ensure_index({ username => 1 }, {
    unique => boolean::true,
    sparse => boolean::false,
});
#die Dumper $res;
$users_coll->insert({ name => 'Foo', username => 'foo' });
eval {
    $users_coll->insert({ name => 'Bar', username => 'foo' });
};
print $@;
eval {
    $users_coll->insert({ name => 'Zorg' });
};
print $@;
eval {
    $users_coll->insert({ name => 'Zorg2' });
};
print $@;


my $us = $users_coll->find;
while  (my $user = $us->next) {
    print Dumper $user;
}



