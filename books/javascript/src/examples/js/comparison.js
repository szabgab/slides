"use strict";

console.log(2 < 3);        // true
console.log('2' < '3');    // true
console.log('a' < 'b');    // true
console.log('c' < 'b');    // false
console.log('-----');

console.log(12 > 3);       // true
console.log(12 > '3');     // true
console.log('12' > 3);     // true
console.log('12' > '3');   // false
console.log('-----');

console.log('a' > '3');    // true
console.log('a' > 3);      // false
console.log('-----');

console.log(null < null);    // false
console.log(null <= null);   // true
console.log('-----');

console.log(null < undefined);   // false
console.log(null <= undefined);  // false
console.log(null > undefined);   // false
console.log(null >= undefined);  // false
