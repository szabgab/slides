use strict;
use warnings;
use Test::More;

use Mock::Quick qw(qclass);
my $control = qclass(
    -implement => 'MyClass',
    -with_new => 1,
    -attributes => [ qw(name) ],
    double => 7,
);


my $obj = MyClass->new;
isa_ok $obj, 'MyClass';

is $obj->name, undef;
is $obj->name('Apple'), 'Apple';
is $obj->name, 'Apple';

is $obj->double(3), 7;


$control->undefine();

done_testing;

