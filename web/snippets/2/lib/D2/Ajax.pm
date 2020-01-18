get '/api/v2/greeting' => sub {
    header 'Access-Control-Allow-Origin' => '*';
    header 'Content-Type' => 'application/json';
    return to_json { text => 'Hello World' };
};
