package App;
use Dancer2;

get '/' => sub {
    return <<'HTML';
<form action="/echo" method="POST">
<input type="text" name="message">
<input type="submit" value="Echo">
</form>
HTML

};

post '/echo' => sub {
    my $message = body_parameters->get('message');
    return "You typed in $message";
};

App->to_app;
