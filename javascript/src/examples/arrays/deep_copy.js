"use strict";

var cases = [
    undefined,
    null,
    42,
    "some string",
    /some reg/,
    ['a', 'b'],
    [
        ['Foo', 23],
        ['Bar', 17]
    ],
    { a: [ 'b', 'c'] }
];
var j;


var deep_copy = function(o) {
    var i;

    if (o === undefined || o === null || typeof o === 'number' || typeof o === 'string' || o instanceof RegExp) {
        return o;
    }
    if (typeof o === 'object') {
        if (Array.isArray(o)) {
            var n = [];
            for (i = 0; i < o.length; i++) {
                n.push(deep_copy(o[i]));
            }
            return n;
        }
    }
    var n = {};
    var keys = Object.keys(o);
    for (i = 0; i < keys.length; i++) {
        n[ keys[i] ] = deep_copy(o[ keys[i] ]);
    }
    return n;
}


for (j = 0; j < cases.length; j++) {
    console.log(j);
    var dc = deep_copy(cases[j]);
    console.log(cases[j]);
    console.log(dc);
    //console.log(dc === cases[j]);
}
