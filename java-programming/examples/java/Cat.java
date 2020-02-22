import java.io.*;

/**
    This class demonstrates how to read a line of text from the keyboard
    Based on http://www.abbeyworkshop.com/howto/java/readLine/ReadLine.java
*/
public class Cat{
    public static void main(String[] args){
        try {
            String CurLine = ""; // Line read from standard in

            InputStreamReader converter = new InputStreamReader(System.in);
            BufferedReader in = new BufferedReader(converter);

            CurLine = in.readLine();
            while (CurLine != null){
                System.out.println(CurLine);
                CurLine = in.readLine();
            }
        }catch (IOException e){
            System.out.println("IO Exception\n");
        }
    }
}

