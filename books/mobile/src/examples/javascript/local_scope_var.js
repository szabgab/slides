name = 'Foo'
console.log(name);    // Foo

function f() {
   console.log(name); // undefined
   var name = 'Bar'
   console.log(name); // Bar
}
f();

console.log(name);    // Foo

