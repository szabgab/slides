export default function fibo(n) {
	if (n == 1) {
		return [1];
	}
	if (n == 2) {
		return [1, 1];
	}
	let numbers = [1]
	for (let c = 3; c <= n; c++) {
		numbers.push(numbers[-1] + numbers[-2]);
	}
	return numbers;
	
}