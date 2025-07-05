import java.io.*;
import java.util.regex.*;

/*
 * Source: http://java.sun.com/docs/books/tutorial/extra/regex/example-1dot4/RegexTestHarness.java
*/

public final class RegexTestHarness {

    private static String REGEX;
    private static String INPUT;
    private static BufferedReader br;
    private static Pattern pattern;
    private static Matcher matcher;
    private static boolean found;

    public static void main(String[] argv) {
        initResources();
        processTest();
        closeResources();
    }

    private static void initResources() {
       try {
           br = new BufferedReader(new FileReader("regex.txt"));
       }
       catch (FileNotFoundException fnfe) {
            System.out.println("Cannot locate input file! "+fnfe.getMessage());
            System.exit(0);
        }
       try {
           REGEX = br.readLine();
           INPUT = br.readLine();
       } catch (IOException ioe) {}

        pattern = Pattern.compile(REGEX);
        matcher = pattern.matcher(INPUT);

        System.out.println("Current REGEX is: "+REGEX);
        System.out.println("Current INPUT is: "+INPUT);
    }

    private static void processTest() {
        while(matcher.find()) {
            System.out.println("I found the text \"" + matcher.group() +
                               "\" starting at index " + matcher.start() +
                               " and ending at index " + matcher.end() + ".");
            found = true;
        }

        if(!found){
            System.out.println("No match found.");
        }
    }

    private static void closeResources() {
       try{
           br.close();
       }catch(IOException ioe){}
    }
}

