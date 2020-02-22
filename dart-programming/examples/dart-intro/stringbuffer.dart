main() {
  StringBuffer sb = new StringBuffer();
  sb.write("Hello");
  sb.writeAll(['space', 'and', 'more']);
 
  print(sb);
  print(sb.toString());
  
  sb.clear();
}