"use strict";

var names = ['Foo', 'Bar', 'Baz'];
console.log(names);         // ["Foo", "Bar", "Baz"]
console.log(names[0]);      // "Foo"

names[3] = 'Moo';
console.log(names[3]);      // "Moo"
console.log(names.length);  // 4

names[6] = "Other";
console.log(names.length);  // 7
console.log(names[4]);      // undefined
console.log(names[6]);      // "Other"
console.log(names);         // [ "Foo", "Bar", "Baz", "Moo", <2 empty slots>, "Other" ]
