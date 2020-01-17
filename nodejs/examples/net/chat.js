var net = require('net');

var sockets = [];

var s = net.Server(function(socket) {
    sockets.push(socket);
    socket.on('data', function(txt) {
        for (var i=0; i < sockets.length; i++) {
            sockets[i].write(txt);
        }
    });
});

s.listen(8000);

