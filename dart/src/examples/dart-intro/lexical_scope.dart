h() {
  print("In external h");
}


f() {
  print("In f");
  g() {
    print("In g");
  }
  h() {
    print("In internal h");
  }

  g();
  h();
}


main() {
  f();
  //g();   // Not declared


  //f() {
  //  print("New f");
  //}

  h();
}
