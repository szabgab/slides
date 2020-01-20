import 'dart:io';

void main() {
    print("What's your name?");
    var name = stdin.readLineSync();
    print("How are you $name, today?");
}
