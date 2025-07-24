"use strict";

var d = new Date;
console.log(d);   // Mon Jul 20 2015 14:46:51 GMT+0300 (IDT)
console.log(Math.abs(new Date() - d));  // 25
setTimeout(show, 10);

d = new Date('1995-12-17T03:24:00');
console.log(d);  // Sun Dec 17 1995 05:24:00 GMT+0200 (IST)

function show() {
    console.log(Math.abs(new Date() - d));  // 618222446613
}
