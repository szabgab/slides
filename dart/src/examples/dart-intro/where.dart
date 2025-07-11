main() {
  List languages = new List();
  languages.add('Perl');
  languages.add('Python');
  languages.add('Dart');
  print(languages);    // [Perl, Python, Dart]

  List short = languages.where((l) => l.length < 5).toList();
  print(short);        // [Perl, Dart]
}