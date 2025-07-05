import java.io.*;
import java.util.regex.*;

/**
    This class demonstrates how to read a line of text from the keyboard
    Based on http://www.abbeyworkshop.com/howto/java/readLine/ReadLine.java
*/
public class Grep{
    public static void main(String[] args){
        try {
            Pattern pattern = Pattern.compile(args[0]);

            String line = ""; 

            InputStreamReader converter = new InputStreamReader(System.in);
            BufferedReader in = new BufferedReader(converter);

            line = in.readLine();
            while (line != null){
                Matcher matcher = pattern.matcher(line);
                if(matcher.find()) {
                    System.out.println(line);
                }
                line = in.readLine();
            }
        }catch (IOException e){
            System.out.println("IO Exception\n");
        }catch (ArrayIndexOutOfBoundsException e){
            System.out.println("Usage: java Grep REGEX   (and then type strings on STDIN, Ctr-D to exit)\n");
        }
    }
}

