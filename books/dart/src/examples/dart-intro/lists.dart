void main() {
  List names = ["Foo", "Bar", "Qux"];
 
  print(names.length);   // 3
  for (var i=0; i < names.length; i++) {
    print(names[i]);
  }
  
  names.add('Zorg');
  print(names);       // [Foo, Bar, Qux, Zorg]

  names.shuffle();    // this is random!
  print(names);       // [Zorg, Foo, Qux, Bar]
  
  print(names.last);  // Bar
  print(names.first); //Zorg
  
  print(names.removeLast()); //Bar
  print(names);              // [Zorg, Foo, Qux]
  
  print(names.removeAt(0)); // Zorg
  print(names);             // [Foo, Qux]

  names.forEach( (v) => print('Value is $v') );
  for (var name in names) {
    print(name);
  }

  // names[4] = 'Abc';  // RangeError: 4
  // print(names[4]);   // RangeError: 4
  // List other = [];
  // print(other.first);  // No elements

}