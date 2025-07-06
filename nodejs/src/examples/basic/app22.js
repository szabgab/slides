const say_hi = require('./lib2');

function other() {
    const say_hello = require('./lib2');
    say_hello('Bar');
}


console.log('Hello World');
say_hi('Foo');

other();


