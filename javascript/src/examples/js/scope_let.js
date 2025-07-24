
let x = 5;

console.log(`before: ${x}`);

{
	//console.log(`inside before: ${x}`); // Uncaught ReferenceError: Cannot access 'x' before initialization
	let x = 6;
	console.log(`inside after: ${x}`);
	x = 7;
	console.log(`inside end: ${x}`);

}

console.log(`outside: ${x}`);
