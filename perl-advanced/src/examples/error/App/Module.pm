package App::Module;
use strict;
use warnings;

use Carp qw(carp cluck);
use App::Code;

sub f {
    my ($x) = @_;
    App::Code::f($x); 
}

sub g {
    my ($x) = @_;
    App::Code::g($x); 
}

sub h {
    my ($x) = @_;
    App::Code::h($x); 
}


1;
