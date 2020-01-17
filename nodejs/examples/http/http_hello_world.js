const http = require('http');     // A subclass of the emitter

const server = http.createServer((req, res) => {
    if (req.url === '/') {
        res.write('Hello World');
        res.end();
    }
});
const port = 3000;

server.listen(port);

console.log(`Listening on port ${port}`);

