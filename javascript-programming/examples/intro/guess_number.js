"use strict";

var hidden = Math.round(Math.random()*200+0.5);
var counter = 0;
console.log(hidden);

function check_guess() {
    counter++;
    var n = Number(document.getElementById('n').value);
    var result = 'equal after ' + counter + ' guesses';
    if (n < hidden) {
        result = n + ' is less than our number';
    }
    if (n > hidden) {
        result = n + ' is greater than our number';
    }
    document.getElementById('result').innerHTML = result;
    return false;
}

document.getElementById('go').addEventListener('click', check_guess);
