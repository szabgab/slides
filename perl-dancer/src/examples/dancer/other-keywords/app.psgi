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
    my $message = query_parameters->get('message');
    return "got DELETE with $message";
};

patch '/mypatch' => sub {
    my $message = body_parameters->get('message');
    return "got PATCH with $message";
};

options '/myoptions' => sub {
    my $message = body_parameters->get('message');
    return "got OPTIONS with $message";
};


App->to_app;
