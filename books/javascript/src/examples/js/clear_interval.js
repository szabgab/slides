"use strict";

function later() {
  console.log('later');
}
function stop() {
    console.log('clearing now');
    clearInterval(timer);
}

var timer = setInterval(later, 1000);
setTimeout(stop, 6000);
console.log('now');
