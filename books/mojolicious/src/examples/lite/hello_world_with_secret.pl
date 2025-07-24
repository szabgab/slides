use Mojolicious::Lite;

get '/' => { text => 'Hello World' };
 
app->secrets(['My very secret passphrase.']);

app->start;
