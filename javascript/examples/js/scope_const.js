
const z = 10;

console.log(`before: ${x}`);

{
	console.log(`inside before: ${x}`);
	const z = 11;
	console.log(`inside after: ${x}`);
	z = 12; // Uncaught TypeError: 
	// console.log(`inside end: ${x}`);

}

console.log(`outside: ${x}`);
