"use strict";

var numbers = [
    '123 124    56',
    '68 23 '
];
var i, j, counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

for (i = 0; i < numbers.length; i++ ) {
    for (j = 0; j < numbers[i].length; j++) {
        if (numbers[i][j] !== ' ') {
            counter[ numbers[i][j] ]++;
        }
    }
}
for (i = 0; i < 10; i++) {
    console.log(i,  counter[i]);
}
