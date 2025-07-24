"use strict";

var name = 'Foo';
var mystr = "Hello " + name + ", how are you?";

console.log(mystr);   // Hello Foo, how are you?
console.log(name);    // Foo

var full = name.concat("Bar");
console.log(name);    // Foo
console.log(full);    // FooBar
