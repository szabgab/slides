"use strict";

var guess = null;
var min = null;
var max = null;
var lower_limit = 1;
var upper_limit = 200;



function start_guessing() {
    min = lower_limit;
    max = upper_limit;
    show();
}
function guess_smaller() {
    max = guess;
    show();
}
function guess_bigger() {
    min = guess;
    show();
}

function bingo() {
    document.getElementById('result').innerHTML = "Yeah!";
    return false;
}

function show() {
    guess = Math.round((max+min)/2);
    document.getElementById('result').innerHTML = guess;
    return false;
}

document.getElementById('go').addEventListener('click', start_guessing);
document.getElementById('bigger').addEventListener('click', guess_smaller);
document.getElementById('smaller').addEventListener('click', guess_bigger);
document.getElementById('bingo').addEventListener('click', bingo);
