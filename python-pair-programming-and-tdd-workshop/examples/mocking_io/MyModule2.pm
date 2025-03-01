package MyModule2;
use strict;
use warnings;

sub game {
    print("Enter your name: ");
    my $name = <STDIN>;
    chomp $name;
    print("Hello '$name'\n");
    print("Guess a number: ");
    my $number = <STDIN>;
    chomp $number;
    print("Your number '$number' is good\n");
    
    return;
}

42;
