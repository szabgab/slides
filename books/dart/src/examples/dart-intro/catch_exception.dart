div(x, y) {
  return x ~/ y;
}

main()  {
  try {
    print(div(2, 1));
    print(div(1, 0));
    print(div(3, 1));
  } catch(exception, stackTrace) {
    print(exception);
    print(stackTrace);
  }
  print("still working");
}