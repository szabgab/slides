"use strict";

var str = "The black cat climbed the green tree.";
console.log(str.substr(5,7));    // lack ca
console.log(str.slice(5,7));     // la

console.log(str.slice(22));      // the green tree.
console.log(str.substr(22));     // the green tree.

console.log(str.slice(10, -10));  // cat climbed the g
console.log(str.substr(10, -10)); // (empty string)

console.log(str.slice(-11, -6)); // green
console.log(str.substr(-11, -6)); // (empty string)

console.log(str.slice(-11, 31));  // green
console.log(str.slice(-11, 50));  // green tree.
console.log(str.substr(-11, 31)); // green tree.
