import 'dart:collection';

main() {
  Queue dentist = new Queue();

  dentist.addLast("Foo");
  dentist.addLast("Bar");
  print(dentist.removeFirst()); // Foo
  print(dentist.removeFirst()); // Bar
}