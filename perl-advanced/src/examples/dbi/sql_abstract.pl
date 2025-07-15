use strict;
use warnings;
use 5.010;

use Data::Dumper qw(Dumper);
use SQL::Abstract;

my $sql = SQL::Abstract->new;

{
    my ($statement, @bind) = $sql->insert('user', {
        username => 'foo',
        email    => 'foo@bar.com',
    });
    say $statement;
    print Dumper \@bind;
}

{
    my ($statement, @bind) = $sql->update('user', {
        username => 'foo',
        email    => 'foo@bar.com',
    });
    say $statement;
    print Dumper \@bind;
}
