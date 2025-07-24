"use strict";

function add() {
    var x = Number(document.getElementById('x').value);
    var y = Number(document.getElementById('y').value);

    document.getElementById('result').innerHTML = x+y;
    return false;
}

document.getElementById('go').addEventListener('click', add);
