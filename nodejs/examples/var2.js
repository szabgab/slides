var x = 1;

console.log(x);      // 1

if (true) {
    console.log(x);  // 1
    var x = 2;
    console.log(x);  // 2
}
console.log(x);      // 2
