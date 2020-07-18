"use strict";

var count = {
    'foo': 23,
    'bar': 42,
    'morse':100
};

console.log(Object.keys(count)); // [ 'foo', 'bar', 'morse' ]

var keys = Object.keys(count);
var i;
for (i = 0; i < keys.length; i++) {
    console.log(i, keys[i], count[ keys[i] ]);
}
// 0 'foo' 23
// 1 'bar' 42
// 2 'morse' 100
