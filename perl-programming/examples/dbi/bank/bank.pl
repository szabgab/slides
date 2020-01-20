#!/usr/bin/perl
use strict;
use warnings;
use 5.010;

use Getopt::Long qw(GetOptions);

my $filename = 'bank.db';

my %opt;
GetOptions(\%opt,
    'create',
) or usage();

if ($opt{create}) {
    create();
}
exit;


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
        CREATE TABLE account (
            id INTEGER PRIMARY KEY,
            owner VARCHAR(100) UNIQUE NOT NULL,
            amount INTEGER DEFAULT 0 NOT NULL 
        )
    });
}
sub delete {
    die "File '$filename' did not exists\n" if not -e $filename;
    unlink $filename or die;
}

sub usage {
    my ($msg) = @_;
    if ($msg) {
        print "\n***** $msg\n\n";
    }
    print <<"END_USAGE";
Usage: $0
   --type   [@types]

   --create
   --delete
   --start name
   --count name

   --help    This help
END_USAGE
   exit();
}

