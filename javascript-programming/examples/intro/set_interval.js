"use strict";

function later() {
    console.log('later');
}

setInterval(later, 1000);
console.log('now');
