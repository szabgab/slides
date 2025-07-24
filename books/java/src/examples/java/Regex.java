import java.io.*;
import java.util.regex.*;

public class Regex{
    public static void main(String[] args){
        {
            String line = "STRING"; 
            Pattern pattern = Pattern.compile("S.R");

            Matcher matcher = pattern.matcher(line);
            if(matcher.find()) {
                System.out.println(line);
                System.out.println("Found '" + matcher.group() +
                               "' starting at index " + matcher.start() +
                               " and ending at index " + matcher.end() + ".");
 
            }else{
                System.out.println("*** NO MATCH ***");
            }
        }
	}
}

