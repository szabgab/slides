"use strict";

function show_selected() {
    var selector = document.getElementById('id_of_select');
    var value = selector[selector.selectedIndex].value;

    document.getElementById('display').innerHTML = value;
}

document.getElementById('btn').addEventListener('click', show_selected);;
