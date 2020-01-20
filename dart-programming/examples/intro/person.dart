class Person {
  double age;
  String name;
  
  Person(this.name);
}

main() {
  var p = new Person("Foo");
  print(p.name);
  p.age = 18.0;
  print(p.age); 
}
