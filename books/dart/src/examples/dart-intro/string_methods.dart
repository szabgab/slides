main () {
  var str = "The black cat climbed the green tree.";
  print(str.contains('The'));                    // true
  print(str.contains('The', 1));                 // false
  print(str.contains(new RegExp(r'dog|cat')));   // true
  
  print(str.indexOf(new RegExp(r'dog|cat'), 2)); // 10
  print(str.indexOf('dog'));                     // -1
  
  print(str.replaceAll('climbed', 'jumped from'));
  print(str);
  
}