"use strict";

var names = new Array("Foo", "Bar", "Moose");
console.log(names);    // [ "Foo", "Bar", "Moose" ]
console.log(names[1]); // "Bar"

var i;
for (i = 0; i < names.length; i++) {
    console.log(names[i]);
}
