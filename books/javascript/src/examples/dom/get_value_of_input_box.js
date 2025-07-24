"use strict";

function clicked() {
    var input_value = document.getElementById('data').value;
    document.getElementById('display').innerHTML = input_value;
}

document.getElementById('btn').addEventListener('click', clicked);;
