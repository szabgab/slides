class MyClass {
    constructor() {
        console.log('object created');
    }
}

function f() {
    const n = new MyClass();
    console.log(n);
}

console.log('before');
f();
console.log('after');
