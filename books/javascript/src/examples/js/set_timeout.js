"use strict";

function later() {
  console.log('later');
}

setTimeout(later, 1000);
console.log('now');
