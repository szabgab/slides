const ping = require("net-ping");

let host = "8.8.8.8";

const session = ping.createSession();
session.pingHost(host, function(error, target) {
    if (error)
        console.log(target + ": " + error.toString());
    else
        console.log(target + ": Alive");
});
