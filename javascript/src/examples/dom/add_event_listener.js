"use strict";

function clicked() {
    document.getElementById('display').innerHTML = 'Hello World';
}

document.getElementById('btn').addEventListener('click', clicked);
