#!/usr/bin/perl 
use strict;
use warnings FATAL => 'all';



package Car;
use strict;
use warnings;

sub new {
    my ($class, $color) = @_;
    my $self = bless {}, $class;

    $self->_init($color);

    return $self;
}

sub _init {
    my ($self, $color) = @_;
    $self->{color} = $color;
}



sub drive {
    my ($self) = @_;
    
}


package SportsCar;
use strict;
use warnings;

use Car;
#our @SportsCar::ISA = ('Car');
our @ISA = ('Car');


#use base 'Car';

sub _init {
    my ($self) = @_;

    $self->SUPER::_init();

}

sub drive {
    my ($self) = @_;
    # 
    $self->SUPER::drive();
    # 
}


package main;

my $trabant = Car->new("White");

my $porsche = SportsCar->new("Red");


$porsche->drive;


