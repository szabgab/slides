package D2::Ajax;
use Dancer2;
use MongoDB ();
use JSON::MaybeXS;
use DateTime::Tiny;
sub DateTime::Tiny::TO_JSON { shift->as_string };

our $VERSION = '0.1';

sub _mongodb {
    my ($collection) = @_;

    my $client = MongoDB::MongoClient->new(host => 'localhost', port => 27017);
    $client->dt_type( 'DateTime::Tiny' );
    my $db   = $client->get_database( config->{app}{mongodb} );
    return $db->get_collection($collection);
}

hook before => sub {
    if (request->path =~ m{^/api/}) {
        header 'Content-Type' => 'application/json';
    }
    if (request->path =~ m{^/api/v[23]/}) {
        header 'Access-Control-Allow-Origin' => '*';
        header 'Access-Control-Allow-Methods' => 'GET, POST, OPTIONS, DELETE';
    }
};

get '/' => sub {
    template 'index';
};

get '/api/v1/greeting' => sub {
    return to_json { text => 'Hello World' };
};

get '/v1' => sub {
    return template 'v1';
};

get '/api/v2/greeting' => sub {
    return to_json { text => 'Hello World' };
};

get '/api/v2/reverse' => sub {
    my $text = param('str') // '';
    my $rev = reverse $text;
    return to_json { text => $rev };
};

post '/api/v2/item' => sub {
    my $text = param('text') // '';
    $text =~ s/^\s+|\s+$//g;
    if ($text eq '') {
        return to_json { error => 'No text provided' };
    }

    my $items = _mongodb('items');
    my $obj = $items->insert({
        text => $text,
        date => DateTime::Tiny->now,
    });
    my $json = JSON::MaybeXS->new;
    $json->convert_blessed(1);
    return $json->encode( { ok => 1, text => $text, id => $obj->to_string } );
};

get '/api/v2/items' => sub {
    my $items = _mongodb('items');
    my @data =  $items->find->all;
    my $json = JSON::MaybeXS->new;
    $json->convert_blessed(1);
    return $json->encode( { items =>  \@data } );
};

del '/api/v2/item/:id' => sub {
    my $id = param('id');

    my $items = _mongodb('items');
    $items->remove({ _id => MongoDB::OID->new($id) });

    my $json = JSON::MaybeXS->new;
    return to_json { ok  => 1 };
};

get '/api/v2/item/:id' => sub {
    my $id = param('id');

    my $items = _mongodb('items');
    my $data = $items->find_one({ _id => MongoDB::OID->new($id) });
    my $json = JSON::MaybeXS->new;
    $json->convert_blessed(1);
    return $json->encode( { item =>  $data } );
};


options '/api/v2/item/:id' => sub {
    return '';
};

######################### v3

post '/api/v3/item' => sub {
    my $text = param('text') // '';
    $text =~ s/^\s+|\s+$//g;
    if ($text eq '') {
        return to_json { error => 'No text provided' };
    }
    my $details = param('details') // '';
    $details =~ s/^\s+|\s+$//g;
    my $id = param('id');
    my $items = _mongodb('items');

    my $obj;
    #debug($text);
    #debug($details);
    if ($id) {
        $obj = MongoDB::OID->new($id);
        $items->update({ _id => $obj }, {
            '$set' => {
                text => $text,
                details => $details,
            }
        });
    } else {
        $obj = $items->insert({
            text => $text,
            date => DateTime::Tiny->now,
        });
    }

    my $data = $items->find_one({ _id => $obj });
    my $json = JSON::MaybeXS->new;
    $json->convert_blessed(1);
    return $json->encode( { ok => 1, item => $data } );
};

get '/api/v3/items' => sub {
    my $items = _mongodb('items');
    my @data =  $items->find->all;
    my $json = JSON::MaybeXS->new;
    $json->convert_blessed(1);
    return $json->encode( { items =>  \@data } );
};

del '/api/v3/item/:id' => sub {
    my $id = param('id');

    my $items = _mongodb('items');
    $items->remove({ _id => MongoDB::OID->new($id) });

    my $json = JSON::MaybeXS->new;
    return to_json { ok  => 1 };
};

get '/api/v3/item/:id' => sub {
    my $id = param('id');

    my $items = _mongodb('items');
    my $data = $items->find_one({ _id => MongoDB::OID->new($id) });
    my $json = JSON::MaybeXS->new;
    $json->convert_blessed(1);
    return $json->encode( { item =>  $data } );
};


options '/api/v3/item/:id' => sub {
    return '';
};

true;
