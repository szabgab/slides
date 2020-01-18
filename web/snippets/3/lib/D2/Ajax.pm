get '/api/v2/reverse' => sub {
    header 'Access-Control-Allow-Origin' => '*';
    header 'Content-Type' => 'application/json';
    my $text = param('str');
    my $rev = reverse $text;
    return to_json { text => $rev };
};
