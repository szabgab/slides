package App;
use Dancer2;
use Time::HiRes ();

get '/' => sub {
    my $db = setting('db');
    return 'TODO';
};

get '/api/add/:text' => sub {
    my $text = route_parameters->get('text');
    my $data = setting('data');
    my $id = int(1000000 * Time::HiRes::time);
    debug "ID: $id";
    my %res = (
        status => 'ok',
        id => $id,
    );

    response_header 'Content-type' => 'application/json';
    return encode_json( \%res );
};

get '/api/get/:id' => sub {
    my $id = route_parameters->get('id');
    send_as JSON => {};
};

get '/api/list' => sub {
    send_as JSON => {};
};

get '/api/del/:id' => sub {
    my $id = route_parameters->get('id');
    send_as JSON => {};
};


hook before => sub {
    set start_time => Time::HiRes::time;
    my $db = $ENV{TODO_DB} || 'todo.json';
    set db => $db;
    #if (not -e $db) {
    #    if (open (my $fh, '>', $db)) {
    #        print $fh encode_json( {} );
    #    }
    #}
    my $data = {};
    if (-e $db) {
        if (open (my $fh, '<', $db)) {
            local $/ = undef;
            my $json_str = <$fh>;
            $data = decode_json( $json_str);
        }
    }
    set data => $data;
};

hook after => sub {
	my ($response) = @_;
    debug $response;

	my $start_time = setting('start_time');
    my $db = setting('db');
    if (open (my $fh, '>', $db)) {
        print $fh encode_json( setting('data') );
    }

	if ($start_time) {
		my $elapsed_time = Time::HiRes::time - $start_time;
        #debug "Elapsed time: $elapsed_time";
        debug $response->{content};
        if ($response->headers->{'content-type'} eq 'application/json') {
            my $json = decode_json($response->{content});
            $json->{elapsed} = $elapsed_time;
            #debug $json;
            $response->{content} = encode_json($json);
        }
	}
	return;
};


App->to_app;

