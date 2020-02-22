//import 'dart:collection';

main() {
  Set english  = new Set();
  english.add('door');
  english.add('car');
  english.add('door');
  english.add('lunar');
  english.add('era');
  print(english.length); // 4
  
  Set spanish = new Set();
  spanish.addAll(['era', 'lunar', 'hola']);
  print(spanish.length); // 3
  print(spanish);        //  {era, lunar, hola}
  
  print(english.intersection(spanish)); //  {lunar, era}
  print(english.difference(spanish));   //  {door, car}
  print(english.union(spanish)); // {door, car, lunar, era, hola}

}