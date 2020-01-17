const fs = require('fs');

fs.appendFile('filename', 'content', (err) => {
    if (err) {
        console.log(err);
    } else {
        console.log('Success');
    }
});
