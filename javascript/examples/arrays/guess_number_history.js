"use strict";

var hidden = Math.round(Math.random()*200+0.5);
var guess_history = [];
var i;

console.log(hidden);

function check_guess() {
    var n = Number(document.getElementById('n').value);
    var result = 'equal after ' + guess_history.length + ' guesses.';
    if (n < hidden) {
        result = n + ' is less than our number';
    }
    if (n > hidden) {
        result = n + ' is greater than our number';
    }
    if (guess_history.length > 0 && n !== hidden) {
        //console.log(guess_history[ ]);
        if (Math.abs(guess_history[guess_history.length - 1] - hidden) < Math.abs(n - hidden)) {
            result += ' (<b>cold</b>)';
        } else {
            result += ' (<b>warm</b>)';
        }
    }
    guess_history.push(n);
    result += '<br>';
    result += '<b>History:</b><br>'
    for (i = guess_history.length-1; i >=0; i--) {
        result += guess_history[i] + '<br>';
    }
    document.getElementById('result').innerHTML = result;
    return false;
}

document.getElementById('go').addEventListener('click', check_guess);
