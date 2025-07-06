const fs = require('fs')

fs.readdir('.', function (err, things) {
    console.log(things)
});
