public class MySubstring {
    public static void main(String[] args) {
        String text = "The black cat climbed the greeen tree.";
        System.out.println(text);
        int textLength = text.length();
        System.out.println(textLength);

        // substring(from)
        String tail = text.substring(textLength-5);
        System.out.println(tail);

        // substring(from, to)
        String word = text.substring(textLength-5, textLength-1);
        System.out.println(word);
    }
}
