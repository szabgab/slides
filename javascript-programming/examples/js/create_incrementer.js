"use strict";

function create_incrementer(n) {
    return function (k) {
        return k+n;
    }
}

var inc_19 = create_incrementer(19);
var inc_17 = create_incrementer(17);
console.log(inc_19(23));  // 42
console.log(inc_17(23));  // 40
