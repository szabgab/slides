"use strict";

var MyThing = function() {
    this.smile = function() {
        console.log("This thing can smile!");
    }
}
var t = new MyThing;
console.log(MyThing); // function MyThing()
console.log(t);       // Object {  }
t.smile();            // "This thing can smile!"
