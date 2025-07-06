
const request = require('request');

//let url = 'http://httpbin.org/get'
let url = 'https://httpbin.org/get'

let options = {
    url: url,
    headers: {
        'User-Agent': 'My Awesone Node browser'
    }
};

request(options, function (error, response, body) {
    if (error) {
        console.log('Something went wrong ', error)
    } else {
        console.log("Status code: " + response.statusCode);
        console.log(response.body);
    }
});

