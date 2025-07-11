import 'dart:html';

void main() {
  print("in main");
  querySelector("#echo").onClick.listen(echoText);
  
  querySelector("#txt").onInput.listen(showText);
}

void showText(Event event) {
  var text = (event.target as InputElement).value;
  querySelector("#echo_place").text = text;
  
}
void echoText(MouseEvent event) {
  var text = querySelector("#txt").value;
  querySelector("#echo_place").text = "You said: $text";
}
