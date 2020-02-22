"use strict";

function greet() {
    document.getElementById('result').innerHTML = 'Hello World';
    return false;
}

document.getElementById('go').addEventListener('click', greet);
