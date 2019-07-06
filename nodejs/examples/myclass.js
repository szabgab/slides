class MyClass{
    constructor() {
        console.log('object created')
    }
}

function f() {
    let n = new MyClass;
}

console.log("before");
f();
console.log("after");

