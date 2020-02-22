main() {
  var operator = '+';
  var a = 23;
  var b = 19;
  
  var c;
  switch(operator) {
    case '+' :
      c = a + b;
      break;
    case '-' :
      c = a - b;
      break;
    default:
      throw("Unknown operator $operator");
  }
  print(c);
}