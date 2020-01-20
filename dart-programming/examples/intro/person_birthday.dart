class Person {
  DateTime birthday;
  String name;
  final int DAYS = 365;
  
  Person(this.name, {this.birthday});
  
  void set age(double years) {
    var d = new DateTime.now();
    var dur = new Duration(days: (DAYS*years).toInt());
    d = d.subtract(dur);
    birthday = d;
  }
  
  double get age {
    var d = new DateTime.now();
    return d.difference(birthday).inDays / DAYS;
  }
  
  double myage() {
    var d = new DateTime.now();
    return d.difference(birthday).inDays / DAYS;   
  }
}

main() {
  var p = new Person("Foo");
  print(p.name);
  p.age = 18.0;
  print(p.age); 
 
  print(p.myage()); // () required because it is not a real getter
  
  var o = new Person("Bar", birthday: new DateTime.now());
  print(o.name);
  print(o.birthday);
}
