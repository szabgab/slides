let x = 1;

console.log(x);      // 1

if (true) {
    //console.log(x);  // ReferenceError: x is not defined
    let x = 2;
    console.log(x);  // 2
}
console.log(x);      // 1

