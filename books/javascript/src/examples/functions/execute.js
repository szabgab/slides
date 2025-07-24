"use strict";

var greeting = function () {
    return "hi there";
}

console.log(greeting);    // [Function]
console.log(greeting());  // hi there

var hw = function () {
    return "Hello World";
}();

console.log(hw);    // Hello World
