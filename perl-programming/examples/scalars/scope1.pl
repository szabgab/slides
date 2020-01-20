#!/usr/bin/perl
use strict;
use warnings;

{
    my $email = 'foo@bar.com';
    print "$email\n";     # foo@bar.com
}
# print $email;
# $email does not exists
# Global symbol "$email" requires explicit package name at ...

