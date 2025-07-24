const fs = require('fs');

fs.readFile('data.txt', 'utf8', (err, content) => {
    if (err) {
        console.log(err);
    } else {
        console.log(content);
    }
});
