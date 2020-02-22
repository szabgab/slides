import 'dart:math' show Random;

void main() {
  var randomizer = new Random(); // can get a seed as a parameter

  // Integer between 0 and 100 (0 can be 100 not)
  var num = randomizer.nextInt(100);
  print(num);
  
  print(randomizer.nextBool());
  var x = "1";
  if (x)
    print("x");
}
