import 'dart:io';

int add(x, y) {
  return x + y;
}

final int z = add(19, 23);
const int q = 4;

main() {
  print(z);
  print(q);
/*  
  print(Platform.environment); // map of environment variables
  print(Platform.environment["PATH"]);
  
  print(Platform.operatingSystem);
  print(Platform.executable);
*/
}