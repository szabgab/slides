const fs = require('fs');

fs.mkdir(dirname, (err) => {

    if (err) {
        console.log(err);
    } else {
        console.log('Success');
    }
});
