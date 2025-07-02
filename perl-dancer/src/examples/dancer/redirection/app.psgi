package App;
use Dancer2;

get '/' => sub {
    return q{
        <html><head><title>Redirection</title></head><body>
        <h1>Main Page</h1>
        <a href="/go/home">Go home</a><br>
        <a href="/go/away">Go away</a><br>
        <a href="/go/elsewhere">Go elsewhere</a><br>
        </body></html>
    };
};

get '/home' => sub {
    return '<h1>Home</h1>Back to the <a href="/">main page</a>';
};


get '/go/:to' => sub {
    my $to = route_parameters->get('to');
    if ($to eq 'home') {
        redirect '/home';
    }
    if ($to eq 'away') {
        redirect 'https://perlmaven.com/';
    }
    return 'Invalid redirect';
};

App->to_app;
