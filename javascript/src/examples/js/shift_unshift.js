"use strict";

var names = [ "foo", "bar", "moo", "qux" ];

var first = names.shift();
console.log(first); //  "foo"
console.log(names); // [ "bar", "moo", "qux" ]

names.unshift("boo");
console.log(names); // [ "boo", "bar", "moo", "qux" ]
