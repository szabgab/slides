"use strict";

console.log(NaN == NaN);          // false

console.log(0 == '0');            // true
console.log(false == '0');        // true
console.log(null == undefined);   // true
console.log(' \t\r\n ' == 0);     // true

console.log('' == '0');           // false
console.log(0 == '');             // true
