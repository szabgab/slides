#!/usr/bin/perl 
use strict;
use warnings;

system "$^X examples/dbi/create_sample.pl";

use DBI;

my $dbfile = "sample.db";

my $dsn = "dbi:SQLite:dbname=$dbfile";
my $dbh = DBI->connect($dsn);

system "$^X examples/dbi/show_accounts.pl before";

debit(1, 100);

system "$^X examples/dbi/show_accounts.pl middle";
#exit;   # process killed

credit(2, 100);

system "$^X examples/dbi/show_accounts.pl account";

sub debit {
    credit($_[0], -1 * $_[1]);
}
sub credit {
    my ($id, $amount) = @_;

    my $sth = $dbh->prepare("SELECT amount FROM accounts WHERE id = ?");
    $sth->execute($id);
    my ($current) = $sth->fetchrow_array();
    $sth->finish;
    $dbh->do("UPDATE accounts SET amount = ? WHERE id = ?",
        undef, $current + $amount, $id);
}

