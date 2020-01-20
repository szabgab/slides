import 'dart:io';        // Platform, File
import 'dart:convert';   // UTF8, ASCII

main() {
  var url = Platform.script;
  print(url);

  var filename = Platform.script.toFilePath();
  print(filename);

  var file = new File(filename);
  var finished = file.readAsLines(encoding: UTF8); 
  finished.then( (text) => text.forEach((line) => print(line) ) );

  //var finished = file.readAsString(encoding: UTF8); 
  //finished.then( (text) => print(text) );
}