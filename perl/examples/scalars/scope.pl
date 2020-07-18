#!/usr/bin/perl
use strict;
use warnings;

my $fname = "Foo";
my $lname = "Bar";
print "$fname\n";        # Foo
print "$lname\n";        # Bar

{
    my $email = 'foo@bar.com';
    print "$email\n";     # foo@bar.com
    print "$fname\n";     # Foo
    print "$lname\n";     # Bar

    my $fname  = "Moo";
    print "$fname\n";     # Moo

    $lname = "Baz";
    print "$lname\n";     # Baz
}
print $email;
# $email does not exists
print "$fname\n";         # Foo
print "$lname\n";         # Baz
