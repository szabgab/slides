use 5.010;
use Moo;
use MooX::Options;

use MongoDB ();
use Data::Dumper qw(Dumper);

option add   => (is => 'ro');
option list  => (is => 'ro');
option update => (is => 'ro');
option delete => (is => 'ro');
option name  => (is => 'ro', format => 's');
option nickname  => (is => 'ro', format => 's');
option phone => (is => 'ro', format => 's');

sub run {
    my ($self) = @_;

    my $client = MongoDB::MongoClient->new(host => 'localhost', port => 27017);
    my $db   = $client->get_database( 'phonebook' );
    my $people_coll = $db->get_collection('people');

    say 'Processing ...';
    if ($self->add) {
        die "--name is needed" if not $self->name;
        die "--phone is needed" if not $self->phone;
        $people_coll->insert( {
            name => $self->name,
            phone => $self->phone,
            nickname => $self->nickname,
        });
    } elsif ($self->list) {
        my %query;
        if ($self->name) {
            $query{name} = $self->name;
        }
        if ($self->phone) {
            $query{phone} = $self->phone;
        }
        my $people = $people_coll->find(\%query);
        while (my $p = $people->next) {
            printf "%s  %s", $p->{name}, $p->{phone};
            if ($p->{nickname}) {
                print " ($p->{nickname})";
            }
            print "\n";
        }
    } elsif ($self->update) {
        die "--name is needed" if not $self->name;
        die "--phone is needed" if not $self->phone;
        
        $people_coll->update(
            { name => $self->name },
            { '$set' => { phone => $self->phone }},
            { multiple => 1 },
        );
    } elsif ($self->delete) {
        die "--name is needed" if not $self->name;
        $people_coll->remove({ name => $self->name });
    } else {
        die "Missing -h, --add,  --list or --update\n";
    }
}
 
main->new_with_options->run;



