"use strict";

console.log(parseInt("0x11"));     //  17

console.log(parseInt("011"));      //  11 or 9 (depends on implementation)
console.log(parseInt("011", 10));  //  11
console.log(parseInt("011", 8));   //  9
console.log(parseInt("011", 16));  //  17
