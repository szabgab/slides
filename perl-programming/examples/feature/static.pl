#!/usr/bin/perl 
use strict;
use warnings;

{
   my $counter = 0;
   sub next_counter {
      $counter++; 
      return $counter;
   }
}

print next_counter(), "\n";
print next_counter(), "\n";

