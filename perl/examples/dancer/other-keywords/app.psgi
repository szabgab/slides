package App;
use Dancer2;

get '/' => sub {
    return <<'HTML';
Try PUT /myput
HTML

};

put '/myput' => sub {
    return "got PUT";
};

del '/mydel' => sub {
    return "got DELETE";
};


App->to_app;
