numbers = [1, 6, 4]
console.log(numbers)         // [1, 6, 4]
console.log(numbers.length)  // 3

for (var i=0; i < numbers.length; i++) {
  console.log(i + ' ' + numbers[i])
}
/*
  0 1
  1 6
  2 4
*/
for (var i in numbers) {
   console.log(i)
}
/*
  0
  1
  2
*/
