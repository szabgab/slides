hi(name) {
  print("Hello $name");
}

var welcome = hi; 

main() {
  hi("Foo");
  welcome("Bar");
}
