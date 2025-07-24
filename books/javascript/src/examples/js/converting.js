"use strict";

var a = "23";
var b = "19";
console.log(a + b); // "2319"
console.log(parseInt(a) + parseInt(b)); // 42

var p = 23;
var q = 19;
console.log(p + q); // 42
console.log(p.toString() + q.toString()); // "2319"
console.log(String(p) + String(q)); // "2319"

console.log(parseInt("23.42"));   // 23
console.log(parseFloat("23.42")); // 23.42

console.log(parseInt("2x3"));     // 2
console.log(parseInt("6.7x3"));   // 6
console.log(parseFloat("4.5x6")); // 4.5

console.log(Number("23"));      // 23
console.log(Number("23.12"));   // 23.12
console.log(Number("2x3"));     // NaN
console.log(Number("6.7x3"));   // NaN
console.log(Number("4.5x6"));   // NaN

