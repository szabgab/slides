"use strict";

var names = ['Foo', 'Bar', 'Morse', 'Foo', 'Bar', 'Luke', 'Lea', 'Han Solo'];

console.log(names.indexOf('Foo'));        // 0
console.log(names.indexOf('Foo', 1));     // 3
console.log(names.lastIndexOf('Foo'));    // 3
console.log(names.lastIndexOf('Foo', 2)); // 0

console.log(names.indexOf('Vader'));      // -1
