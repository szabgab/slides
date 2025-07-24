"use strict";

var sum = function () {
    var i, s = 0;
    for (i=0; i < arguments.length; i++) {
        s += arguments[i];
    }
    return s;
}
console.log(sum(2, 5, 1)); // 8
