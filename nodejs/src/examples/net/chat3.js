const net = require('net');

var sockets = [];

const sock = net.Server(function(socket) {
    sockets.push(socket);
    socket.on('data', function(txt) {
        for (var i = 0; i < sockets.length; i++) {
            if (sockets[i] === socket) continue;
            sockets[i].write(txt);
        }
    });
    socket.on('end', function() {
        var i = sockets.indexOf(socket);
        sockets.splice(i, 1);
    });
});

sock.listen(8000);

