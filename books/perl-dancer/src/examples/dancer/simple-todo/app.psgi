package App;
use Dancer2;
use Time::HiRes ();

get '/' => sub {
    return 'TODO';
};

get '/api/add/:text' => sub {
    my $text = route_parameters->get('text');
    my $data = vars->{'data'};
    my $id = int(1000000 * Time::HiRes::time);
    #debug "ID: $id";
    $data->{$id} = $text;
    save_data(vars->{'db'}, $data);
    my %res = (
        status => 'ok',
        id => $id,
    );

    response_header 'Content-type' => 'application/json';
    return encode_json( \%res );
};

get '/api/get/:id' => sub {
    my $id = route_parameters->get('id');

    my %res;
    my $data = vars->{'data'};
    if (exists $data->{$id}) {
        %res = (
            id => $id,
            text => $data->{$id},
            status => "ok",
        );
    } else {
        status 'not_found';
        %res = (
            "id" => $id,
            "status" => "failure",
        );
    }

    response_header 'Content-type' => 'application/json';
    return encode_json( \%res );

};

get '/api/list' => sub {
    my $data = vars->{'data'};
    my %res = (
        status => 'ok',
        items => [ map { { id => $_, text => $data->{$_} } }  keys %$data ],
    );
    response_header 'Content-type' => 'application/json';
    return encode_json( \%res );
};

get '/api/del/:id' => sub {
    my $id = route_parameters->get('id');

    my %res;
    my $data = vars->{'data'};
    if (exists $data->{$id}) {
        %res = (
            id => $id,
            text => $data->{$id},
            status => "ok",
        );
        delete $data->{$id};
        save_data(vars->{'db'}, $data);
    } else {
        status 'not_found';
        %res = (
            "id" => $id,
            "status" => "failure",
        );
    }


    response_header 'Content-type' => 'application/json';
    return encode_json( \%res );
};


hook before => sub {
    var start_time => Time::HiRes::time;
    my $db = $ENV{TODO_DB} || 'todo.json';
    var db => $db;

    my $data = {};
    if (-e $db) {
        if (open (my $fh, '<', $db)) {
            local $/ = undef;
            my $json_str = <$fh>;
            $data = decode_json( $json_str);
        }
    }
    var data => $data;
};

hook after => sub {
	my ($response) = @_;
    #debug $response;

	my $start_time = vars->{'start_time'};

	if ($start_time) {
		my $elapsed_time = Time::HiRes::time - $start_time;
        #debug "Elapsed time: $elapsed_time";
        #debug $response->{content};
        if ($response->headers->{'content-type'} eq 'application/json') {
            my $json = decode_json($response->{content});
            $json->{elapsed} = $elapsed_time;
            #debug $json;
            $response->{content} = encode_json($json);
        }
	}
	return;
};

sub save_data {
    my ($db, $data) = @_;
    if (open (my $fh, '>', $db)) {
        print $fh encode_json( $data );
    }
}

App->to_app;

