main() {
  List numbers = [1, 2, 3];
  print(numbers);      // [1, 2, 3]
  
  var doubles = numbers.map((val) => 2 * val);
  print(doubles);  // (2, 4, 6)
  
  
  var double_list = doubles.toList();
  print(double_list);  // [2, 4, 6]
}
