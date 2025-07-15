package OverdraftAccount;
use 5.010;
use Moose;

our $VERSION = '0.01';

extends 'BankAccount';

has 'limit' => (
    is       => 'ro',
    isa      => 'Num',
    required => 1,
);



1;
