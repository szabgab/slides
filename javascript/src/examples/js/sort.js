"use strict";

var names = ['Foo', 'Bar', 'Moose', 'Zorg', 'Baz', 'Moo'];
console.log(JSON.stringify(names, undefined, 2));
//  ['Foo', 'Bar', 'Moose', 'Zorg', 'Baz', 'Moo'];

names.sort();
console.log(JSON.stringify(names, undefined, 2));
//  ['Bar', 'Baz', 'Foo', 'Moo', 'Moose', 'Zorg'];

var numbers = [3, 12, 4];
console.log(JSON.stringify(numbers, undefined, 2));
// [3, 12, 4];
numbers.sort();
console.log(JSON.stringify(numbers, undefined, 2));
// [12, 3, 4];

numbers.sort(function(a, b) { return a-b });
console.log(JSON.stringify(numbers, undefined, 2));
// [3, 4, 12];

var names = ['Foo', 'Bar', 'Moose', 'Zorg', 'Baz', 'Moo'];
names.sort(function(a, b) { return a.length - b.length });
console.log(JSON.stringify(names, undefined, 2));
// ['Foo', 'Bar', 'Baz', 'Moo', 'Zorg', 'Moose'];

names.sort(function(a, b) { return a.length - b.length || a.localeCompare(b)});
console.log(JSON.stringify(names, undefined, 2));
// ['Bar', 'Baz', 'Foo', 'Moo', 'Zorg', 'Moose'];
