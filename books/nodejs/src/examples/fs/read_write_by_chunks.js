const fs = require('fs');

const readStream = fs.createReadStream('README', 'utf8'); // inherits from events
const writeStream = fs.createWriteStream('README.txt');
readStream.on('data', (chunk) => {
    if (chunk) {
        writeStream.write(chunk);
    }
});
