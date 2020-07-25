package App;
use Dancer2;

get '/' => sub {
    return '<a href="/user/1">One</a> <a href="/user/2">Two</a>';
};

get '/user/:id' => sub {
    my $id = param('id');
    if ($id > 1) {
        status 'not_found';
        return 'No such ID';
    }
    return $id;
};

App->to_app;
