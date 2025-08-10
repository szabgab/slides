use Mojolicious::Lite;
use Mojo::JSON qw(decode_json);
use FindBin;
use DBI;
use DBIx::Simple;

get '/' => sub {
    my $c = shift;
    $c->stash( urls => [
        [ '/api/v1/greeting' => 'GET no CORS'],
        [ '/v1'              => 'HTML demo page'],
        [ '/api/v2/greeting' => 'GET woth CORS'],
        [ '/v2'              => 'HTML demo page'],

        [ '/api/v2/reverse'  => 'GET with ?text=TEXT'],

        [ '/api/v2/items'    => 'GET returning list of items'],
        [ '/api/v2/item'     => 'POST expecting {text => TEXT}'],
        [ '/api/v2/item/ID'  => 'DELETE where ID is the id number of an item'],
    ]);
    $c->render( template => 'index' );
};

get '/v1' => sub {
    my $c = shift;
    $c->render( template => 'greeting', version => 'v1' );
};

get '/v2' => sub {
    my $c = shift;
    $c->render( template => 'greeting', version => 'v2' );
};


get '/api/v1/greeting' => {
    json => {
        text => 'Hello World from Mojolicious'
    }
};

under sub {
    my $c = shift;

    # 'Access-Control-Allow-Origin' => '*';
    $c->res->headers->access_control_allow_origin('*');

    # 'Access-Control-Allow-Headers' => 'Content-Type';
    $c->res->headers->append('Access-Control-Allow-Headers' => 'Content-Type');

    # 'Access-Control-Allow-Methods' => 'POST';
    $c->res->headers->append('Access-Control-Allow-Methods' => 'GET, POST, OPTIONS, DELETE');
};

get '/api/v2/greeting' => sub {
    my $c = shift;
    $c->render( json => {
        text => 'Hello World from Mojolicious with CORS enabled'
    });
};

get '/api/v2/reverse' => sub {
    my $c = shift;
    $c->render( json => {
        text => scalar reverse $c->param('str'),
    });
};

options '/api/v2/item' => sub {
    my $c = shift;
    $c->render( json => {nothing => ''} );
};
options '/api/v2/item/:id' => {
    json => {nothing => ''}
};

post '/api/v2/item' => sub {
    my $c = shift;
    my $data = decode_json $c->req->body;
    
    get_db()->query('INSERT INTO items (text, date) VALUES (?, ?)', $data->{text}, time);
    $c->render( json => {
        text => $data->{text},
    });
};

del '/api/v2/item/:id' => sub {
    my $c = shift;
    my $id = $c->param('id');
    $c->app->log->debug("delete $id");
    my $res = get_db()->query('DELETE FROM items WHERE id=?', $id)->rows;
    $c->app->log->debug("deleted $id: $res");
    if ($res) {
        $c->render( json => {
            ok => 1
        });
    } else {
        #$c->reply->not_found;
        $c->render( json => {
            text => 'No such item',
                },
            status => 404,
        )
    }
};


get '/api/v2/items' => sub {
    my $c = shift;
    my @items = get_db()->query('SELECT * FROM items')->hashes;
    $c->render( json => {
        items => \@items,
    });
};

sub get_db {
    my $dbfile = "$FindBin::Bin/items.db";
    if (not -e $dbfile) {
        my $dbh = DBI->connect("dbi:SQLite:dbname=$dbfile","","");
        $dbh->do(q{CREATE TABLE items (
            id      INTEGER PRIMARY KEY,
            text    VARCHAR(255),
            date    VARCHAR(10)
        )
        });
    }
    return DBIx::Simple->connect("dbi:SQLite:dbname=$dbfile","","", {
        RaiseError => 1,
        PrintError => 0,
        AutoCommit => 1,
    });
}

app->secrets(['My very secret passphrase.']);
app->start;

__DATA__

@@ index.html.ep

<html>
 <head>
   <title>Back-end for building Single Page Applications</title>
 </head>
<body>
<h1>Back-end for building Single Page Application</h1>

<table>
  <tr><th>URL</th><th>Explanation</th></tr>
% for my $u (@$urls) {
  <tr><td><a href="<%= $u->[0] %>"><%= $u->[0] %></a></td><td><%= $u->[1] %></td></tr>
% } 
</table>
</body>
</html>

@@ greeting.html.ep
 
<html ng-app="DemoApp" ng-controller="DemoController">
  <head>
      <script src="angular.min.js"></script>
      <title><%= $version %></title>

<script>
angular.module('DemoApp', [])
.controller('DemoController', ['$scope', '$http', function($scope, $http) {
    $scope.title = 'Static Title';
    $http({
        method: 'GET',
        url: '/api/<%= $version %>/greeting'
    }).then(function(response) {
        console.log('success', response);
        $scope.greeting = response.data.text;
    }, function(response) {
        console.log('failure', response);
    });
}]);
</script>

  </head>
<body>
<h1>{{title}}</h1>
<h2>{{greeting}}</h2>
</body>
</html>
