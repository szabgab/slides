div(x, y) {
  return x ~/ y;
}

main()  {
  try {
    print(div(2, 1));
    print(div(1, 0));
    print(div(3, 1));
  } on StateError catch(exception, stackTrace) {
  } on ArgumentError catch(e) {
  } catch(exception, stackTrace) {
    print(exception);
    print(stackTrace);
  } finally {
    print("Runs no matter what");
  }
  print("still working");
}
