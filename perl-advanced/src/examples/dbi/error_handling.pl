$sth = $dbh->prepare($statement)   or die $dbh->errstr;
$rv  = $sth->execute(@bind_values) or die $sth->errstr;

