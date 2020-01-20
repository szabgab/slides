"use strict";

var names = [
    ['Foo', 23],
    ['Bar', 17]
];

var other = names.concat('Joe');
console.log(names);    // [ [ 'Foo', 23 ], [ 'Bar', 17 ] ]
console.log(other);    // [ [ 'Foo', 23 ], [ 'Bar', 17 ], 'Joe' ]

names[0][0] = 'Moooo';
console.log(names);    // [ [ 'Moooo', 23 ], [ 'Bar', 17 ] ]
console.log(other);    // [ [ 'Moooo', 23 ], [ 'Bar', 17 ], 'Joe' ]
