const http = require('http');

const server = http.createServer((req, res) => {
    if (req.url === '/') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write('Hello World <a href="/api/users">users</a>');
        res.end();
    }
    if (req.url === '/api/users') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.write(JSON.stringify([1, 2, 3]));
        res.end();
    }
});
const port = 3000;

server.listen(port);

console.log(`Listening on port ${port}`);
