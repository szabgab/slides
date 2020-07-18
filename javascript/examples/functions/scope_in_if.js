"use strict";

var x = 42;
console.log(x);       // 42
if (true) {
    var x = 23;       // var does not do anything here
    console.log(x);   // 23
}
console.log(x);       // 23
