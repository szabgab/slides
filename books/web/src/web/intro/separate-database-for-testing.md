# Use separate database for testing

config.yml


```
app:
  mongodb: d2-ajax
```

lib/D2/Ajax.pm


```
my $db   = $client->get_database( config->{app}{mongodb} );
```

t/v2.t


```
my $db_name = 'd2-ajax-' . $$ . '-' . time;
diag $db_name;
D2::Ajax->config->{app}{mongodb} = $db_name;
```

Drop the database automatically


```
use MongoDB ();
```

```
my $client = MongoDB::MongoClient->new(host => 'localhost', port => 27017);
my $db   = $client->get_database( $db_name );
$db->drop;
```
