const fs = require('fs');

fs.rename('old.txt', 'new.txt', (err) => {
    if (err) {
        console.log(err);
    } else {
        console.log('Success');
    }

});


