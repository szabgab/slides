main() {
  int i = 0;
  while (i < 3) {
    i++;
    print(i);
  }
  
  print('----');
  while(true) {
    i++;
    if (i > 7) {
      break;
    }
    if (i == 5) {
      continue;
    }
    print(i);
  }
}
