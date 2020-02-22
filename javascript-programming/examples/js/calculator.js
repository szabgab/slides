"use strict";

function calculate() {
    var x = Number(document.getElementById('x').value);
    var y = Number(document.getElementById('y').value);
    var op = document.getElementById('op').value;
    var result;

    switch (op) {
        case '+' : {
            result = x+y;
            break;
        };
        case '*' : {
            result = x*y;
            break;
        };
        case '-' : {
            result = x-y;
            break;
        };
        case '/' : {
            result = x/y;
            break;
        };
    };

    document.getElementById('result').innerHTML = result;
    return false;
}

document.getElementById('go').addEventListener('click', calculate);
