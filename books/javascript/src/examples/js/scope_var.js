
var x = 3;


{
	console.log(`inside before: ${x}`);
	var x = 4;
	console.log(`inside after: ${x}`);
}

console.log(`outside: ${x}`);
