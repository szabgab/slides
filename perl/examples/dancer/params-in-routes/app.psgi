package App;
use Dancer2;

get '/' => sub {
    return '<a href="/user/1">One</a> <a href="/user/2">Two</a>';
};

get '/user/:id' => sub {
    my $id = route_parameters->get('id');
    return $id;
};

App->to_app;
