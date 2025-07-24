main() {
  List languages = ['Perl', 'Python', 'Dart']; 
  print(languages);    // [Perl, Python, Dart]

  print(languages.any((l) => l.length < 5));  // true
  
}