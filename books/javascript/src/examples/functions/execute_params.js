"use strict";

var greeting = function (name) {
    return "hi " + name;
}

console.log(greeting);         // [Function]
console.log(greeting('Foo'));  // hi Foo

var hw = function (name) {
    return "Hello " + name;
}('Bar');

console.log(hw);    // Hello Bar
