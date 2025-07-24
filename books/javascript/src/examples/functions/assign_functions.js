"use strict";

var add = function (a, b) {
    return a+b;
}

var sum = add;

console.log(add(2, 3));  // 5
console.log(sum(3, 4));  // 7

console.log(sum);        // [Function]
// function add(a, b) {
//     return a+b;
// }
