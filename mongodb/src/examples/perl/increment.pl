use strict;
use warnings;
use 5.010;

use MongoDB ();
use Data::Dumper qw(Dumper);

my $client = MongoDB::MongoClient->new(host => 'localhost', port => 27017);
my $db   = $client->get_database( 'example_' . time  );

my $collection = $db->get_collection('counters');

$collection->insert( { _id => 'posts', seq => 0 });
say inc('posts');
say inc('posts');
say inc('posts');
say inc('posts');
say inc('posts');

sub inc {
    my ($field) = @_;
    $collection->find_and_modify( {
        query  => { _id => $field },
        update => { '$inc' => { seq => 1 } },
        new  => 1,  # to return the new value
                    # by default it returns the old value
    } )->{seq}
}

$db->drop;

