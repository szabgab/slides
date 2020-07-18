"use strict";

var MyThing = function() {
}
var t = new MyThing;
console.log(MyThing); // function MyThing()
console.log(t); // Object {  }

t.a = 23;
console.log(t);
t.doit = function() {
    console.log('doit');
    console.log(this);
    console.log(this.a);
}
t.doit();
