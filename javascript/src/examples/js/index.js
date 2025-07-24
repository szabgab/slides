"use strict";

var str = "The black cat climbed the green tree.";
console.log(str.indexOf('a'));         // 6
console.log(str.indexOf('a', 7));      // 11
console.log(str.lastIndexOf('t'));     // 32
console.log(str.lastIndexOf('t', 31)); // 22

console.log(str.indexOf('cat'));       // 10
console.log(str.indexOf('dog'));       // -1
