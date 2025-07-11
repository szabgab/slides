create_incrementor(num inc) {
  incrementor(num) {
    return num + inc;
  }
  return incrementor;
}

main() {
  var inc17 = create_incrementor(17);
  print(inc17(3));   // 20

  var inc23 = create_incrementor(23);
  print(inc23(19)); // 42
}
