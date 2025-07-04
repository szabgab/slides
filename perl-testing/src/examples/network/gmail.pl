#!/usr/bin/perl
use strict;
use warnings;

use WWW::GMail;

my $w = WWW::GMail->new(
    username => "USERNAME",
    password => "PASSWORD",
);

my $ret = $w->login();
if ($ret == -1) {
    die "password incorrect\n";
} elsif ($ret == 0) {
    die "unable to login $w->{error}\n";
}

my @messages = $w->get_message_list('inbox');
foreach my $msg (@messages) {
    print "Subject: $msg->[6]\n";
}
