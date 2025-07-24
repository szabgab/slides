use Mojolicious::Lite;

use Data::Dumper qw(Dumper);
use DBIx::Simple;
use FindBin;

my $dbfile = $ENV{TODODB} || "$FindBin::Bin/todo.db";
my $has_db = -e $dbfile;
my $db = DBIx::Simple->connect("dbi:SQLite:dbname=$dbfile", '', '', {
    RaiseError => 1,
    PrintError => 0,
    AutoCommit => 1,
});
if (not $has_db) {
    $db->query(q{
        CREATE TABLE tasks (
            id       INTEGER  PRIMARY KEY,
            title    VARCHAR(255),
            details  BLOB,
            created  DATE     default CURRENT_TIME,
            due      DATE,
            status   BOOLEAN  default 'waiting',
            priority INTEGER
        )
    });
}

get '/' => sub {
    my $c = shift;
    $c->render( 'index' )
};

get '/list' => sub {
    my $c = shift;
    my @tasks = $db->query('SELECT * FROM tasks')->hashes;
    $c->stash(tasks => \@tasks);
    $c->render( 'list' )
};

get '/add' => sub {
    my $c = shift;
    $c->render( 'add' )
};


post '/save' => sub {
    my $c = shift;
    $db->query(q{INSERT INTO tasks (title, details, priority) VALUES (?, ?, ?)}, $c->param('title'), $c->param('details'), $c->param('priority'));
    $c->stash( title => 'Added' );
    $c->render( 'added' );
};

get '/task/:id' => sub {
    my $c = shift;

    my ($task) = $db->query('SELECT * FROM tasks WHERE id=?', $c->param('id'))->hash;
    $c->app->log->debug(Dumper $task);
    $c->stash( task => $task, title => $task->{title} );
    $c->render( 'task' );
};
    

app->start;

__DATA__
@@ index.html.ep
% layout 'wrapper';
% title 'TODO';

<h1>Welcome to the TODO application</h1>


@@ list.html.ep
% layout 'wrapper';
% title 'Listing TODO items';

<table>
% for my $t (@$tasks) {
    <tr>
       <td><a href="/task/<%= $t->{id} %>"><%= $t->{title} %></a></td>
       <td><a href="/edit/<%= $t->{id} %>">e</a></td>
    </tr>
% }
</table>

@@ added.html.ep
% layout 'wrapper';

<h1>Added</h1>


@@ add.html.ep
% layout 'wrapper';
% title 'TODO';

<form method="post" action="/save">
<input type="text" name="title" size="80"><br>
<textarea name="details" rows="6" cols="80"></textarea><br>
Priority <select name="priority">
<option value="">No priority</option>
<option value="1">1</option>
<option value="2">2</option>
<option value="3">3</option>
</select><br>
<input type="submit" value="Save">
</form>


@@ task.html.ep
% layout 'wrapper';

<h1><%= $task->{title} %></h1>
<div id="details"><%= $task->{details} %></div>
Priority: <%= $task->{priority} %>


@@ layouts/wrapper.html.ep
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport"
     content="width=device-width, initial-scale=1, user-scalable=yes">
  <title><%= title %></title>

<style>
html,body {
  margin-top: 0;
  margin-left: 10px;
  margin-right: 10px;
  padding: 0;
}
#menu {
  margin-top: 10px;
  margin-bottom: 10px;
  font-weight:bold;
}
#menu ul {
  list-style: none;
  display: inline;
}
#menu li {
  margin-left: 10px;
  float: left;
}
#menu a {
  text-decoration:none;
}
</style>

</head>

<body>
<div id="menu">
<ul>
  <li><a href="/">home</a></li>
  <li><a href="/add">Add</a></li>
  <li><a href="/list">List</a></li>
</ul>
</div>

<%= content %>

</body>
</html>


