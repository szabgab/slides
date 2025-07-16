#!/usr/bin/perl
use strict;
use warnings;

print "Hello, I am Foo, what's your name ? ";
$name = <STDIN>;
chomp $name;
print "Hi $name, what is the size of your shoes ? ";
$size = <STDIN>;
chomp $size;

if ($size >= 40 and $age <= 45 ) {
   print "Then please go to the second floor\n";
   
}

if ($size < 40 or $age > 45 ) {
   print "Sorry we don't have anything in your size.\n";
}
