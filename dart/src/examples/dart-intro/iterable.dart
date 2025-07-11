main() {
 var numbers = new Iterable.generate(5, (i) => i);
 print(numbers.length);
 print(numbers);
 
 for (var n in numbers) {
   print(n);
 }
}