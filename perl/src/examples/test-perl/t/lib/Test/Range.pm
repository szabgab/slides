package Test::Range;
use strict;
use warnings;

our $VERSION = '0.01';

use base 'Exporter';
our @EXPORT = qw(is_between);
use Test::Builder;

use Carp qw(croak);

my $Test = Test::Builder::Module->builder;

=head2 is_between

is_between ($lower_limit, '<', $real_value, '<=', $name);

=cut
sub is_between {
    my ($lower_limit, $op1, $real_value, $op2, $upper_limit, $name) = @_;
    croak "The comparison operators ($op1)must all be either < or <="
        if $op1 ne '<' and $op1 ne '<=';
    croak "The comparison operators ($op2)must all be either < or <="
        if $op2 ne '<' and $op2 ne '<=';
    croak "The lower limit must be lower than the upper limit"
        if $lower_limit >= $upper_limit;

    $name ||= '';

    my @errors;
    if (($op1 eq '<' and not $lower_limit < $real_value)
        or ($op1 eq '<=' and not $lower_limit <= $real_value)) {
            push @errors, "Lower limit: $lower_limit $op1 $real_value failed";
    }
    if (($op2 eq '<' and not $real_value < $upper_limit)
        or ($op2 eq '<=' and not $real_value <= $upper_limit)) {
            push @errors, "$real_value $op2 $upper_limit upper limit failed";
    }

    $Test->ok(! scalar @errors, $name)
        or $Test->diag(join "", map {"         $_\n"} @errors);
}

1;


