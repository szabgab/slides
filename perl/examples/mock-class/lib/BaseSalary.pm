package BaseSalary;
use strict;
use warnings;

sub new {
    my ($class) = @_;
    print "new\n";
    my $self = bless {}, $class;

    return $self;
}

# plain getter/setter for name (with an extra print statement)
sub name {
    my ($self, $value) = @_;
    print "name\n";
    if (@_ == 2) {
        $self->{name} = $value;
    }
    return $self->{name};
}

sub get_base_salaray {
    my ($self) = @_;
    print "get_base_salary\n";

    return 1370;
}

1;

