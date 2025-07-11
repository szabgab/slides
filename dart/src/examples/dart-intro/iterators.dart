main () {
  var names = ['Foo', 'Bar', 'Qux'];

  for (var n in names) {
    print(n);
  }
  
  print('----');
  var it = names.iterator;
  while (it.moveNext()) {
    var n = it.current;
    print(n);
  }
}
