"use strict";

var names = ['Foo', 'Bar'];

console.log(names.concat({ x:'y'})); // [ 'Foo', 'Bar', { x: 'y' } ]
console.log(names.concat(/regex/));  // [ 'Foo', 'Bar', /regex/ ]
