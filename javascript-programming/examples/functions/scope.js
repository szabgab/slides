"use strict";

var x = 42;

var add = function (a, b) {
    var x = a + b;      // private x
    return x;
}

var multiply = function (a, b) {
    x = a * b;          // global x
    return x;
}

console.log(x);              // 42
console.log(add(2, 3));      //  5
console.log(x);              // 42
console.log(multiply(2, 4)); //  8
console.log(x);              //  8
