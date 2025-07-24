"use strict";

var MyPerson = function(fname) {
    this.first_name = fname;
}

var m = new MyPerson('Foo');
console.log(MyPerson); // function MyPerson()
console.log(m);        // Object {  }
