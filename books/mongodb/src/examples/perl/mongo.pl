use strict;
use warnings;

use MongoDB;
use DateTime;
use Data::Dumper qw(Dumper);

my $conn = MongoDB::Connection->new;
my $db = $conn->demo;
my $users = $db->users;

my %user;
if (0) {
    %user = (
        fname => 'Gabor',
        lname => 'Szabo',
        added => DateTime->now,
    );
}

if (1) {
    %user = (
        fname => 'Foo',
        lname => 'Bar',
        added => time,
    );
}

if (0) {
    print $users->insert(\%user), "\n";
}

if (1) {
    #print Dumper $users->find_one({ fname => 'Gabor' });
    #my $cursor = $users->find({ added => { '$lt' => time }});
    my $cursor = $users->find();
    while ( my $doc = $cursor->next ) {
        print Dumper $doc;
    }
}
