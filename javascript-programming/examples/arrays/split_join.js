"use strict";

var names = ['Foo', 'Bar', 'Morse', 'Foo', 'Bar', 'Luke', 'Lea', 'Han Solo'];

var str = names.join(':');
console.log(str); // Foo:Bar:Morse:Foo:Bar:Luke:Lea:Han Solo

var n = str.split(':');
console.log(n);
// [ 'Foo', 'Bar', 'Morse', 'Foo', 'Bar', 'Luke', 'Lea', 'Han Solo' ]
