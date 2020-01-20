"use strict";

var x = {
  'a' : 1,
  'b' : 2
};
console.log(x);           // Object {a: 1, b: 2}
var ret = delete(x['a']);
console.log(x);           //Object {b: 2}
console.log(ret);         // true

var ret = delete(x['c']);
console.log(x);           //Object {b: 2}
console.log(ret);         // true
