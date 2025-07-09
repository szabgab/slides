use strict;
use warnings;
use 5.010;


# http://stackoverflow.com/questions/15139999/mongodb-index-an-internal-list-of-objects
# http://stackoverflow.com/questions/6743849/mongodb-unique-index-on-array-elements-property

use MongoDB ();
use Data::Dumper qw(Dumper);

my $client = MongoDB::MongoClient->new(host => 'localhost', port => 27017);
my $db   = $client->get_database( 'training' );
$db->drop;

# without sparse we can get one document without the indexed field
# with spars=true we can get more such documents
my $users_coll = $db->get_collection('users');
my $res = $users_coll->ensure_index({ 'emails.address' => 1 }, {
    unique => boolean::true,
    sparse => boolean::false,
});
#die Dumper $res;
$users_coll->insert({ name => 'Foo', emails => [
   {
      name => 'bat',
      address => 'foobar.com',
   },
   {
      name => 'foo',
      address => 'foobar.com',
   }
] });

my $res1 = $users_coll->update({name=>'Foo'}, {
    '$push', {
        'emails' => {
            name => 'Joe',
            address => 'joe@ex.com',
        }
    }
});

my $res2 = $users_coll->update({name=>'Foo'}, {
    '$push', {
        'emails' => {
            name => 'Joe2',
            address => 'joe@ex.com',
        }
    }
});


#my $u = $users_coll->find_one({name=>'Foo'});
#print Dumper $u;
#__END__

my $us = $users_coll->find;
while  (my $user = $us->next) {
    print Dumper $user;
}


