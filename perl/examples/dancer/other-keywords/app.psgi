package App;
use Dancer2;

get '/' => sub {
    return <<'HTML';
Try PUT /myput
HTML

};

put '/myput' => sub {
    my $message = body_parameters->get('message');
    return "got PUT with $message";
};

del '/mydel' => sub {
    return "got DELETE";
};

patch '/mypatch' => sub {
    return "got PATCH";
};

options '/myoptions' => sub {
    return "got OPTIONS";
};


App->to_app;
