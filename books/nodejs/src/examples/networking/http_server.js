const http = require('http')

http.createServer(function(req, res) {
    res.writeHead(200, 'Header');
    res.write('Reply\n');
    let html = '<html><head><title>Title</title></head><body></body></html>';
    res.write(html);
    res.set
    res.end();
}).listen(8080);

