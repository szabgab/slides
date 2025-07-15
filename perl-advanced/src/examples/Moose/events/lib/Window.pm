package Window;
use Moose;

with 'Timer';

use Event;

has events => (
    is      => 'rw',
    isa     => 'ArrayRef[Event]',
    default => sub { [] },
);

sub event {
    my $self = shift;
    push @{ $self->events }, Event->new(); # TODO pass arguments
}

1;

