var http = require('http');   // Load the http library

var s = http.createServer(function(req, res) {
    res.writeHeader(200, { 'Content-Type' : 'text/plain' });
    res.write('Hello\n');
    setTimeout(function() {
        res.end('World\n');
    }, 2000);

});

s.listen(8000);


