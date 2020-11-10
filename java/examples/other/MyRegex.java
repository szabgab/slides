import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class MyRegex {
    public static void main(String[] args) {
        String[] emails = {"abc@corporate.com", "demo-id12@corporate.com", "demo-id12@other.com"};
        Pattern pattern = Pattern.compile("demo-id[0-9]+@corporate\\.com$");
        for (int i=0; i < emails.length; i++) {
            System.out.println(emails[i]);
            Matcher matcher = pattern.matcher(emails[i]);
            if (matcher.find()) {
                System.out.println("OK");
            }
        }
    }
}
