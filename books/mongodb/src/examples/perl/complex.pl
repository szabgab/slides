use strict;
use warnings;
use 5.010;

use MongoDB ();
use Data::Dumper qw(Dumper);

my $client = MongoDB::MongoClient->new(host => 'localhost', port => 27017);
my $db   = $client->get_database( 'example_' . $$ . '_' . time  );
END {
    $db->drop if $db;
}

my $people_coll = $db->get_collection('people');

$people_coll->insert( {
    name => 'First',
    phones => [
        {
            type   => 'home',
            number => '1-123',
        },
        {
            type   => 'work',
            number => '1-456',
        }
    ],
});
_dump();


# replace the whole section of 'phones'
$people_coll->update(
    { name => 'First' },
    { '$set' => {
            phones => [
                {
                    type => 'mobile',
                    number => '1-789',
                }
            ]
        }
});
_dump();

# add another phone to the list
$people_coll->update(
    { name => 'First' },
    { '$push' => {
            phones => 
                {
                    type => 'work',
                    number => '2-789',
                }
        }
});
_dump();

$people_coll->update(
    { name => 'First', 'phones.type' => 'mobile' },
    { '$set' => {
            'phones.$.number' => '1234', 

        }
    }
);
_dump();

$people_coll->update(
    { name => 'First', 'phones.type' => 'mobile' },
    { '$set' => {
            'phones.$.number' => '5678',
            'phones.$.extension' => '120',
        }
    }
);
_dump();


sub _dump {
    print Dumper $people_coll->find->all;
}

__END__
$people_coll->remove({ name => $self->name });
