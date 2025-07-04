package CLIDaemon::Connection;
use strict;
use warnings;
use 5.008;

our $VERSION = '0.01';

use base 'Class::Accessor';
__PACKAGE__->mk_accessors(qw(username password state));

sub new {
    my $self = bless {}, $_[0];
    $self->state("username");
    return $self;
}

sub prompt {
    my ($self) = @_;
    if ($self->state eq "username") {
        print "Username: ";
    } elsif ($self->state eq "password") {
        print "Password: ";
    } elsif ($self->state eq "basic") {
        print "cli> ";
    } elsif ($self->state eq "enabled") {
        print "cli> ";
    } else {
        print "Invalid mode";
        exit;
    }
}




1;


