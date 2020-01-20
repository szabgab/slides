"use strict";

var names = ['Foo', 'Bar', 'Moo'];
var people = ['Joe', 'Mary'];

var joint_list = names.concat(people, 'Morgo', ['Bare', 'Array']);
console.log(names);       // [ 'Foo', 'Bar', 'Moo' ]
console.log(people);      // [ 'Joe', 'Mary' ]
console.log(joint_list);
// [ 'Foo', 'Bar', 'Moo', 'Joe', 'Mary', 'Morgo', 'Bare', 'Array' ]
