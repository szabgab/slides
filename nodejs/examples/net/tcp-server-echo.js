var net = require('net');

var server = net.createServer(function(socket) {
    socket.write("hello\n");
    socket.write("world\n");
    socket.on('data', function(data) {
       socket.write('You said: ' + data);
    })
});

server.listen(8000);

