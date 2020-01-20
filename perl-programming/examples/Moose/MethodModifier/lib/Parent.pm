package Parent;
use Moose;

has name => (is => 'rw', isa => 'Str', required => 1);

sub welcome {
    my $self = shift;
    print "Hello " . $self->name, "\n";
    return 'welcome';
}


sub nick {
    my $self = shift;
    print "Start hi " . $self->name, "\n";
    print "inner ret: " . inner() . "\n";
    print "End hi " . $self->name, "\n";
    return 'nick';
}

sub show_name {
}

before show_name => sub {
    print "Before show_name\n";
};

after show_name => sub {
    print "After show_name\n";
};


1;

