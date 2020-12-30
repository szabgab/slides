const http = require('http');

url = 'http://httpbin.org/get';

http.get(url, (res) => {
  const { statusCode } = res;

  console.error("StatusCode " + statusCode);
  if (statusCode !== 200) {
    console.log("Error");
    // Consume response data to free up memory
    res.resume();
    return;
  }

  let rawData = '';
  res.on('data', (chunk) => { rawData += chunk; });
  res.on('end', () => {
    console.log(rawData);
    });
});
