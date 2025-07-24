String prompt(String text, [int count = 1]) {
  for (int i = 0; i < count; i++) {
    print(text);
  }
}

void main() {
    prompt("Your name:", 3);
    prompt("Your Cat:");
}
