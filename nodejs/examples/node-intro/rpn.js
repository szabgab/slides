const assert = require('assert');

//const input_list = [2, 3, "+"]
//console.log(input_list) 
//console.log(input_list.length()) 
//

function calc(a, op, b) {
    if (op == '+') {
        return a + b;
    }
    throw "Unsupported operator";
}

console.log(calc(2, '+', 3))
assert(calc(2, '+', 3) == 5)
assert(calc(2, '*', 3) == 6)

