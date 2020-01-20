main() {
  var str = "Hello"  "World";
  print(str);        // HelloWorld
  str += " of Dart";
  print(str);        // HelloWorld of Dart
  
  print(str.length); // 18 
  
  print(str[0]);    // H
  
  var here = """
    Multi-line string
    instead of Here documents.
  """;
  print(here);
  
  
  var regular = 'regular strings \d \n\w';
  var raw = r'raw strings \d \n\w for regex';
  print(regular); // regular strings d 
                  // w
  print(raw);     // raw strings \d \n\w for regex
}