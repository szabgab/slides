"use strict";

function create_counter(start, step) {
    var n;
    return function () {
        if (n === undefined) {
            n = start;
            return n;
        }
        n += step;
        return n;
    }
}

var count_by_3 = create_counter(1, 3);
var count_by_7 = create_counter(2, 7);

console.log(count_by_3());  // 1
console.log(count_by_3());  // 4
console.log(count_by_3());  // 7
console.log(count_by_7());  // 2
console.log(count_by_7());  // 9
console.log(count_by_7());  // 16
console.log(count_by_3());  // 10
console.log(count_by_7());  // 23
