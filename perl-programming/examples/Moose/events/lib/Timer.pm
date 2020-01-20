package Timer;
use Moose::Role;

use Time::HiRes qw(time);

has start_time => (
     is => 'rw', 
     isa => 'Str',
     default => sub { time },
);
has end_time   => (
     is => 'rw',
     isa => 'Str',
);

# not yet ended
sub active {
     my $self = shift;
     return ! $self->end_time;
}

sub end {
    shift->end_time(time);
}


1;

