name = 'Foo'
console.log(name);    // Foo

function f() {
   console.log(name); // Foo
   name = 'Bar'
   console.log(name); // Bar
}
f();

console.log(name);    // Bar
