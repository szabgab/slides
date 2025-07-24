"use strict";

var dispatch_table = {
    '+' : function (a, b) {
        return a+b;
    },
    '-' : function (a, b) {
        return a-b;
    }
};

function run(dt, op, x, y) {
    if (! dt[op]) {
        console.log("Invalid operator: " + op);
        return;
    }
    return dt[op](x, y);
}

console.log(run(dispatch_table, '-', 2, 3));  // -1
console.log(run(dispatch_table, '+', 2, 3));  // 5
console.log(run(dispatch_table, '*', 2, 3));  // Invalid operator: *
