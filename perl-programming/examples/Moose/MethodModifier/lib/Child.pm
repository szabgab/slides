package Child;
use Moose;

extends 'Parent';

# the return values of before and after are discarded. So no point in returning any value
before welcome => sub {
    my $self = shift;
    print "Before " . $self->name . "\n";
};

after welcome => sub {
    my $self = shift;
    print "After " . $self->name . "\n";
};
    

around welcome => sub {
    my $orig = shift;
    my $self = shift;

    print "Around before call\n";
    my $ret = $self->$orig;
    print "After before call\n";

    return 'around';
};

augment nick => sub {
    my $self = shift;
    print "Augumented nick " . $self->name . "\n";
    return 'augumented';    
};

override show_name => sub {
    print "show_name in child\n";
};


1;

