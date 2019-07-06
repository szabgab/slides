let x = 1;

console.log(x);      //

if (true) {
    console.log(x);  //
    var x = 2;       // SyntaxError: Identifier 'x' has already been declared
    console.log(x);  //
}
console.log(x);      //
