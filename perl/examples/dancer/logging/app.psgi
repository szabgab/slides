package App;
use Dancer2;

set format_message => '%h %L %T - %m';
# https://metacpan.org/pod/Dancer2::Core::Role::Logger
#

get '/' => sub {
    debug "debug main";
    info "info main";
    warning "main";
    error "main";

    return 'Hello World!';
};

App->to_app;
