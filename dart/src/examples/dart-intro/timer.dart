import 'dart:async';

main() {
  new Timer(new Duration(seconds: 1), () => print("timeout"));
  print("end main");
}