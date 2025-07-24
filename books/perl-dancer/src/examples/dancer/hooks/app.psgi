package App;
use Dancer2;
use Time::HiRes ();

get '/' => sub {
    my $db = vars->{'db'};
    return "DB: $db<br>PLACEHOLDER";
};

hook before => sub {
    var start_time => Time::HiRes::time;
    var db => 'database.json';
};

hook after => sub {
	my ($response) = @_;  # Dancer2::Core::Response
	my $start_time = vars->{'start_time'};
    debug $response;

	if ($start_time) {
		my $elapsed_time = Time::HiRes::time - $start_time;
        debug "Elapsed time: $elapsed_time";
        $response->{content} =~ s/PLACEHOLDER/Elapsed time: $elapsed_time/;
	}
	return;
};


App->to_app;




