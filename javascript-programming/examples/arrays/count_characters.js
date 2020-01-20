"use strict";

var string = "hello world";
var i, j;
var counter = [];
var chars = [];

for (i = 0; i < string.length; i++) {
    // console.log(string[i]);
    var found = false;
    for (j = 0; j < chars.length; j++) {
        if (chars[j] == string[i]) {
            counter[j]++;
            found = true;
            break;
        }
    }
    if (! found) {
        chars.push(string[i]);
        counter.push(1);        
    }
}

for (i = 0; i < chars.length; i++) {
    console.log(chars[i],  counter[i]);
}
