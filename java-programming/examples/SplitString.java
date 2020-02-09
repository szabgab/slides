import java.util.*;
/**
 *  This class demonstrates how to use the StringTokenizer class to split apart
 *  strings of text.
 *  Source: http://www.abbeyworkshop.com/howto/java/splitString/SplitString.java
 */
class SplitString {
    public static void main(String[] arguments) {
        StringTokenizer ex1, ex2; // Declare StringTokenizer Objects
        int count = 0;

        String strOne = "one two  three      four   five";
        ex1 = new StringTokenizer(strOne); //Split on Space (default)

        while (ex1.hasMoreTokens()) {
            count++;
            System.out.println("Token " + count + " is [" + ex1.nextToken() + "]");
        }

        count = 0;     // Reset counter

        String strTwo = "item one,item two,item three,item four"; // Comma Separated
        ex2 = new StringTokenizer(strTwo, ",");  //Split on comma

        while (ex2.hasMoreTokens()) {
            count++;
            System.out.println("Token " + count + " is [" + ex2.nextToken() + "]");
        }
    }
}
