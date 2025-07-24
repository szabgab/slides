"use strict";

var text = 'this is a constructor this is not';

var words = text.split(/\s+/);
var count = {};
var i;
for (i in words) {
    var word = words[i];
    if (count[word] === undefined) {
        count[word] = 0;
    }
    count[word]++;
}
console.log(count);
// Object { this: 2, is: 2, a: 1, constructor: NaN, not: 1 }
