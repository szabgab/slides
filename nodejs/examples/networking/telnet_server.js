const telnet = require('telnet');

telnet.createServer(function(client) {
//    client.on("error", function(err) {
//        //console.log(err.stack);
//        console.log(
//    });
    client.write('My banner');
    client.do.window_size();
}).listen(8080);

