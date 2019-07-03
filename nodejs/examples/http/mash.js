setInterval(function() {
    console.log("world");
}, 5000);

var http = require('http');
setInterval(function() {
    console.log("fetching google.com");
    http.get({ host: 'google.com' }, function(res) {
        console.log(res.headers);
    });
}, 2000);

console.log("hello");

