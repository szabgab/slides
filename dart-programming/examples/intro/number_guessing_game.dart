import 'dart:math' show Random;
import 'dart:io';

void main() {
  var MAX = 200;
  var randomizer = new Random();
  var num = randomizer.nextInt(MAX);
  print(num);
  while (true) {
    print("Please guess a number between 0 and $MAX:");
    var guess = stdin.readLineSync();
    if (guess == 'x')
      break;
    if (guess == num)
      print("Success");
  }
    
  print("Goodbye");
}
