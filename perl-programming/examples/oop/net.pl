#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/lib';
use My::Net::Device;
use My::Net::Router;
use My::Net::Interface;
use English qw( -no_match_vars ) ;

my $device = My::Net::Device->new({id => 1});
print "$device\n";
print $device->get_id, "\n";
print $device->_debug;
eval {
    $device->get_id(2);
};
warn "WARN: $EVAL_ERROR" if $EVAL_ERROR;

my $router = My::Net::Router->new({id => 3});
foreach my $i (0..3) {
    my $interface = My::Net::Interface->new({id => $i});
    $router->add_interface($interface);
}
print $router->_debug;

