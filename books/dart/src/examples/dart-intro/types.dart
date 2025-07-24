add(x, y) {
  return x+y;
}

main() {
  var name;       // null
  dynamic z = 1; // the same as var, not used

  int age;        // null
  double o7;      // null
  bool isit;      // null
  String email;   // null

  name = 'Foo';
  name = 'Bar';
  

  const address = 'New York';
  //address = "Moscow";
  const double pi = 3 + 0.14;
  final int answer = add(19, 23);
    
  print(z);        // 1
  z++;
  print(z);        // 2
  print(pi);       // 3.14
  print(answer);   // 42
}
