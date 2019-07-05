const fs = require('fs');

fs.writeFile('data.txt', 'first line', (err) => {
    if (err) {
        console.log(err);
    } else {
        console.log('Success');
    }
});

