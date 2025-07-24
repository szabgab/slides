"use strict";

var str = "Hello World";
console.log(str[0]);        // H
console.log(str[1]);        // e
console.log(str.charAt(0)); // H
console.log('----');

var i;
for (i = 0; i < str.length; i++) {
    console.log(str[i]);
}

console.log(str.slice(3, 7));  // lo W
