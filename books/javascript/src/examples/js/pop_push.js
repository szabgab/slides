"use strict";

var names = [ "foo" ];
console.log(names);   // [ "foo" ]

names[1] = "bar";
console.log(names);   // [ "foo", "bar" ]

names.push("moo");
console.log(names);  // [ "foo", "bar", "moo" ]

names.push("qux", "zorg");
console.log(names); // [ "foo", "bar", "moo", "qux", "zorg" ]

var last = names.pop();
console.log(last);  // "zorg"
console.log(names); // [ "foo", "bar", "moo", "qux" ]
