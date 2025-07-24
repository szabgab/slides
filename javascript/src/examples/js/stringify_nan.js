"use strict";

var x = 2/0;
var y = -2/0;
var z = x+y;
var n = null;

console.log(JSON.stringify({ "x" : x }, undefined, 2));
console.log(JSON.stringify({ "y" : y }, undefined, 2));
console.log(JSON.stringify({ "z" : z }, undefined, 2));
console.log(JSON.stringify({ "n" : n }, undefined, 2));
