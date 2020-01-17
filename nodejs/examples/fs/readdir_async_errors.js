const fs = require('fs')

fs.readdir('xyz', function (err, files) {
    if (err) {
        console.log('Error', err);
    } else {
        console.log(files);
    }
})

