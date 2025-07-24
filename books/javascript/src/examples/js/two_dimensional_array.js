"use strict";

var entries = [
    ["Foo", 123],
    ["Bar", 345],
    ["Moo", 230],
];
var i;
for (i = 0; i < entries.length; i++) {
    console.log(entries[i][0] + ' - ' + entries[i][1]);
}

// Foo - 123
// Bar - 345
// Moo - 230
