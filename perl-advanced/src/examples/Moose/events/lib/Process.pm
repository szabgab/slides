package Process;
use Moose;
use 5.008;
use autodie;

use Session;

has file => (is => 'ro', isa => 'Str');
has err  => (is => 'ro', isa => 'GlobRef');

has sessions => (
    is      => 'rw',
    isa     => 'ArrayRef[Session]',
    default => sub { [] },
);


sub run {
    my $self = shift;
    open my $fh, '<', $self->file;
    while (my $line = <$fh>) {
       chomp $line;
       my ($cmd, @args) = split / /, $line;
       $self->$cmd(@args);
    }
    $self->end_window;  #imply
    $self->end_session; #imply 
}

sub start_session {
    my $self = shift;

    if (defined $self->sessions->[-1] and $self->sessions->[-1]->active) {
        print {$self->err} "start_session while previous session is still active\n"; # TODO what about windows?
        $self->sessions->[-1]->imply_end;
    }
    push @{ $self->sessions }, Session->new(@_);
    return;
}

sub end_session {
    my $self = shift;

    if (not defined $self->sessions->[-1]) {
       print {$self->err} "end_session without session in $.\n";
       return;
    }
    if ( not $self->sessions->[-1]->active) {
       print {$self->err} "end_session without active session in $.\n";
       return;
    }
    $self->sessions->[-1]->end(@_);   
    return;
}

sub start_window {
    my $self = shift;

    if (not defined $self->sessions->[-1]) {
       print {$self->err} "start_window without session in $.\n";
       return;
    }
    if ( not $self->sessions->[-1]->active) {
       print {$self->err} "start_window without active session in $.\n";
       return;
    }
    $self->sessions->[-1]->start_window(@_);

    return;
}

sub end_window {
    my $self = shift;

    if (not defined $self->sessions->[-1]) {
       print {$self->err} "end_window without session in $.\n";
       return;
    }
    if ( not $self->sessions->[-1]->active) {
       print {$self->err} "end_window without active session in $.\n";
       return;
    }
    my $window = $self->sessions->[-1]->windows->[-1];
    if (not $window) {
       print {$self->err} "end_window without window in $.\n";
       return;
    }
    if (not $window->active) {
       print {$self->err} "end_window without active window in $.\n";
       return;
    }
    $window->end(@_);

    return;
}


sub event {
    my $self = shift;

    if (not defined $self->sessions->[-1]) {
       print {$self->err} "event without session in $.\n";
       return;
    }
    if ( not $self->sessions->[-1]->active) {
       print {$self->err} "event without active session in $.\n";
       return;
    }
    my $window = $self->sessions->[-1]->windows->[-1];
    if (not $window) {
       print {$self->err} "event without window in $.\n";
       return;
    }
    if (not $window->active) {
       print {$self->err} "event without active window in $.\n";
       return;
    }
    $window->event(@_);
}

sub out {
    my $self = shift;

    my $out = '';
    foreach my $session (@{ $self->sessions }) {
        $out .= 'session  ' . $session->start_time . '  ' . $session->end_time . "\n";
        foreach my $window (@{ $session->windows }) {
            $out .=  '     window ' . $window->start_time . '  ' . $window->end_time . "\n";
            foreach my $event (@{ $window->events }) {
               $out .= '        event ' . $event->start_time . "\n";
            }
        }
    }
    return $out;
}



1;


