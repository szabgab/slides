import 'dart:convert';

var person = {
         "name" : "Foo Bar",
         "emails" : ["foo@bar.com", "foobar@gmail.com"],
         "phone" : "1234",
};

main () {
  print(person);
  String person_in_json = JSON.encode(person);
  print(person_in_json);
  
  print(person_in_json.length);  // 77
  print(person.length);  // 3
}

