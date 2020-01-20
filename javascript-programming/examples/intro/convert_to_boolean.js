"use strict";

var x = undefined;
console.log(x);  // undefined

var y = !! x;
console.log(y);  // false


x = "hello";
console.log(x);  // hello
y = !! x;
console.log(y);  // true
