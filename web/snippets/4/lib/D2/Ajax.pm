hook before => sub {
    if (request->path =~ m{^/api/}) {
        header 'Content-Type' => 'application/json';
    }
    if (request->path =~ m{^/api/v2/}) {
        header 'Access-Control-Allow-Origin' => '*';
    }
};
