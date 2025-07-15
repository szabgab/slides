#!/usr/bin/perl 
use strict;
use warnings;


my %phone_of = (
    Foo    => '123-foo',
    Bar    => '123-bar',
    Baz    => '123-baz',
    Moo    => '123-moo',
);

print "$phone_of{Foo}\n";

my @phones = ($phone_of{Foo}, $phone_of{Bar});

@phones = @phone_of{'Bar', 'Baz'};

@phones = @phone_of{ qw(Bar Baz) };

my @selected_people = qw(Bar Baz); 
@phones = @phone_of{ @selected_people };

print "@phones\n";

