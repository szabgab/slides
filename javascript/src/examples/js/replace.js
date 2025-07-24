"use strict";

var str = "The black cat climbed the green tree.";
var dog = str.replace("cat", "dog");
console.log(str); // The black cat climbed the green tree.
console.log(dog); // The black dog climbed the green tree.

var str = str.replace("cat", "tiger");
console.log(str); // The black tiger climbed the green tree.

var str = str.replace("black", "");
console.log(str); // The  tiger climbed the green tree.

var str = str.replace(" ", "");
console.log(str); // The tiger climbed the green tree.
