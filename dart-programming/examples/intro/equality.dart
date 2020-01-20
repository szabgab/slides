void main() {
  var x = 23;
  var y = "23";
  if (x == y) 
    print("string and int are not equal");

  if (x == int.parse(y)) 
    print("Converted string equals to int");

  if (x.toString() == y)
    print("Int converted to string also works");
}
