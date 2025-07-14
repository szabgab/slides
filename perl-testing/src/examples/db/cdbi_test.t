#!/usr/bin/perl
use strict;
use warnings;

use MyUsers;
use Test::More qw(no_plan);

my @users = MyUsers->search(fname => 'Gabor');
is(@users, 1);

foreach my $user (@users) {
    is($user->email, 'gabor@pti.co.il');
}

