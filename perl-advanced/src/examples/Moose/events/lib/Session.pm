package Session;
use Moose;

with 'Timer';

use Window;

has windows => (
    is => 'rw',
    isa => 'ArrayRef[Window]',
    default => sub { [] },
);


sub start_window {
    my $self = shift;
    push @{ $self->windows }, Window->new;
    return;
}

sub imply_end {
    my $self = shift;
    $self->end;
}

1;

