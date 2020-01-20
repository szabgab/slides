my %attributes = (
    PrintError  => 1,
    RaiseError  => 1,
    AutoCommit  => 1,
    FetchHashKeyName => 'NAME_lc',  #   NAME_uc
    TraceLevel  => 1,  # see Debugging and Trace levels later
);

my $dsn = "dbi:SQLite:dbname=$dbfile";
my $dbh = DBI->connect($dsn, $username, $password, \%attributes);
