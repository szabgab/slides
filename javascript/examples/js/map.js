"use strict";

var numbers = [2, 5, 3, 7];
function double(n) {
    return n*2;
}

var doubles = numbers.map(double);
console.log(numbers);  // [2,  5, 3,  7]
console.log(doubles);  // [4, 10, 6, 14]

var triples = numbers.map(function(n) { return n * 3 });
console.log(triples);  // [6, 15, 9, 21]
