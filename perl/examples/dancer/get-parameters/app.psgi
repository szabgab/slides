package App;
use Dancer2;

get '/' => sub {
    return <<'HTML';
<form action="/echo" method="GET">
<input type="text" name="message">
<input type="submit" value="Echo">
</form>
HTML

};

get '/echo' => sub {
    my $message = query_parameters->get('message');
    return "You typed in $message";
};

App->to_app;
