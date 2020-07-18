package Counter::DBI;
use strict;
use warnings;
use 5.010;

my $filename = "counter.db";

use DBI;

sub _connect {
    return DBI->connect("dbi:SQLite:dbname=$filename", "", "", {
        AutoCommit => 1,
        RaiseError => 1,
        PrintError => 0,
        FetchHashKeyName => 'NAME_lc',
    });
}

sub create {
    die "File '$filename' already exists\n" if -e $filename;
    my $dbh = _connect();
    $dbh->do(q{
        CREATE TABLE counter (
            name VARCHAR(100) UNIQUE NOT NULL,
            count INTEGER DEFAULT 0 NOT NULL 
        )
    });
}

sub start {
    my ($name) = @_;
    my $dbh = _connect();
    my $sth = $dbh->prepare('SELECT COUNT(*) FROM counter WHERE name = ?');
    $sth->execute($name);
    my ($counter) = $sth->fetchrow_array;

    die "Name '$name' already exists\n" if $counter;
    $dbh->do('INSERT INTO counter (name) VALUES (?)', undef, $name);
    say 0;
}

sub count {
    my ($name) = @_;
    my $dbh = _connect();
    my $sth = $dbh->prepare('SELECT count FROM counter WHERE name = ?');
    $sth->execute($name);
    my ($count) = $sth->fetchrow_array;

    die "Name '$name' does not exist\n" if not defined $count;
    $count++;
    say $count;
    $dbh->do('UPDATE counter SET count = ? WHERE name = ?', undef, $count, $name);
}

sub delete {
    die "File '$filename' did not exists\n" if not -e $filename;
    unlink $filename or die;
}

1;
