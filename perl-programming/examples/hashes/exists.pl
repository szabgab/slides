#!/usr/bin/perl 
use strict;
use warnings;

my %phones;
$phones{Foo} = '111';
$phones{Bar} = '222';
$phones{Moo} = undef;

print defined $phones{Foo} ? "Foo: $phones{Foo}\n" : "Foo not defined\n";
print defined $phones{Moo} ? "Moo: $phones{Moo}\n" : "Moo not defined\n";
print defined $phones{Baz} ? "Baz: $phones{Baz}\n" : "Baz not defined\n";

print exists $phones{Moo}  ? "Moo exists\n"        : "Moo does not exist\n";
print exists $phones{Baz}  ? "Baz exists\n"        : "Baz does not exist\n";

delete $phones{Foo};
print exists $phones{Foo}  ? "Foo exists\n"        : "Foo does not exist\n";


