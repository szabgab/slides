var prompt = require('prompt');

prompt.start();

prompt.get(['fname', 'lname'], function (err, result) {
    var fname = result.fname;
    var lname = result.lname;
    console.log('Command-line input received:');
    console.log('  fname: ' + fname);
    console.log('  lname: ' + lname);
    prompt.get(['email'], function (err, result) {
        var email = result.email;
        console.log('Internal:');
        console.log('  fname: ' + fname);
        console.log('  lname: ' + lname);
        console.log('  email: ' + email);
    });
});
