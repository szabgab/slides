const fs = require('fs');

fs.unlink(filename, (err) => {
    if (err) {
        console.log(err);
    } else {
        console.log('Success');
    }
});
