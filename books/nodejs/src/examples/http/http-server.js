var http = require('http');   // Load the http library

var s = http.createServer(function(req, res) {
    res.writeHeader(200, { 'Content-Type' : 'text/plain' });
    res.end('Hello World\n');

});

s.listen(8000);

