const fs = require('fs');

fs.rmdir(dirname, (err) => {
    if (err) {
        console.log(err);
    } else {
        console.log('Success');
    }
});
