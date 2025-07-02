package App;
use Dancer2;

get '/' => sub {
    return q{
        <a href="/api/1">api/1</a><br>
    };
};

get '/api/1' => sub {
    my %data  = (
        name => 'Dancer',
        language => 'Perl',
    );
    send_as JSON => \%data;
};

get '/api/2' => sub {
    my %data  = (
        name => 'Dancer2',
        language => 'Perl 7',
    );
    send_as JSON => \%data,
        { content_type => 'application/json; charset=UTF-8' };
};

get '/api/3' => sub {
    my %data  = (
        answer => 42,
    );
    push_header 'Content-type' => 'application/json';
    return encode_json( \%data );
};



App->to_app;




