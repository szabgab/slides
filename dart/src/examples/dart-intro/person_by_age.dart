class Person {
  DateTime birthday;
  String name;
  final int DAYS = 365;
  
  Person(this.name, {this.birthday});

  Person.byAge(this.name, double years) {
    var d = new DateTime.now();
    var dur = new Duration(days: (DAYS*years).toInt());
    d = d.subtract(dur);
    birthday = d;
  }  
}

main() {
  var p = new Person.byAge("Foo", 18.0);
  print(p.name);
  print(p.birthday); 
  
  var o = new Person("Bar", birthday: new DateTime.now());
  print(o.name);
  print(o.birthday);
}
