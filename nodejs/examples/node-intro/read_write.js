const fs = require('fs');

const readStream = fs.createReadStream('README', 'utf8'); // inherits from events
const writeStream = fs.createWriteStream('README.txt');
readStream.pipe(writeStream);
