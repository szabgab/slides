package MySalary;
use strict;
use warnings;

use BaseSalary;

sub get_salary {
    my ($name) = @_;

    my $bonus = 100;

    my $obj = BaseSalary->new;
    $obj->name($name);
    my $base_salary = $obj->get_base_salary();

    return $base_salary + $bonus;
}

1;


