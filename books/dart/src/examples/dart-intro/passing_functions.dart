doSomething(List values, Function func) {
  for (var v in values) {
    var r = func(v);
    print("Input: $v Output: $r");
  }
}

double_num(n) {
   return 2*n; 
}

main() {
  doSomething([1, 2, 3], (n) => n*n);

  doSomething([4, 5], double_num);
}
