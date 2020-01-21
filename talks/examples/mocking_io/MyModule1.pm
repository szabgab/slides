package MyModule1;
use strict;
use warnings;

sub game {
    print("Enter your name: ");
    my $name = <STDIN>;
    chomp $name;
    print("Hello '$name'\n");

    return;
}

42;
