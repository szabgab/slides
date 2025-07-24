"use strict";

var x = true;
var y = true;
var z = false;
var q = false;

console.log(x && y); // true
console.log(x && z); // false
console.log('-----');

console.log(x || y); // true
console.log(x || z); // true
console.log(z || x); // true
console.log(z || q); // false
console.log('-----');

console.log(! x); // false
console.log(! z); // true
