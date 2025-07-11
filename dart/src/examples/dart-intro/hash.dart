main() {
  Map joe = {
     "name"  : "Joe",
     "email" : "joe@somewhere.com" 
  };
  print(joe); // {name: Joe, email: joe@somewhere.com} 
  
  joe.putIfAbsent('email', () => 'a@b.com');
  print(joe); // {name: Joe, email: joe@somewhere.com}
  joe.putIfAbsent('birthdate', () => new DateTime.now());
  print(joe);
  // {name: Joe, email: joe@somewhere.com, birthdate: 2014-02-25 20:53:04.548}

  print(joe.containsKey('email')); // true
}