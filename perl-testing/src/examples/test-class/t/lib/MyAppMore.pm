package t::lib::MyAppMore;
use strict;
use warnings;

use base 'Test::Class';
use Test::More;
use Time::HiRes qw(time);

use MyApp qw(add div);

sub test_add : Test {
    my ($self) = @_;
    diag "st add: $self->{start_time}";

    is add(2, 3), 5, 'more add';
}

sub test_div : Test {
    my ($self) = @_;
    diag "st div: $self->{start_time}";

    is div(6, 3), 2, 'more div';
}


sub setup_fixture : Test(setup) {
    my ($self) = @_;   # t::lib::MyAppMore instance
    $self->{start_time} = time;
    diag "setup $self->{start_time}";
}

sub teardown_fixture : Test(teardown) {
    my ($self) = @_;
    my $end_time = time;
    diag "teardown elapsed time: " . ($end_time - $self->{start_time});
}


sub startup_fixture : Test(startup) {
    my ($self) = @_;
    $self->{class_start_time} = time;
    diag "startup $self->{class_start_time}";
}
sub shutdown_fixture : Test(shutdown) {
    my ($self) = @_;
    my $end_time = time;
    diag "shutdown elapsed time: " . ($end_time - $self->{class_start_time});
}



1;
