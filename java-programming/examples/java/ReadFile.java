import java.io.*;

/**
    Source: http://www.abbeyworkshop.com/howto/java/readFile/ReadFile.java
*/

public class ReadFile{
    public static void main(String[] args){
        try {
			
			/*	Sets up a file reader to read the file passed on the command
				line one character at a time */
			FileReader input = new FileReader(args[0]);
            
			/* Filter FileReader through a Buffered read to read a line at a
			   time */
			BufferedReader bufRead = new BufferedReader(input);
			
            String line; 	// String that holds current file line
            int count = 0;	// Line number of count 
            
            // Read first line
            line = bufRead.readLine();
            count++;
            
			// Read through file one line at time. Print line # and line
            while (line != null){
                System.out.println(count+": "+line);
                line = bufRead.readLine();
                count++;
            }
            
            bufRead.close();
			
        }catch (ArrayIndexOutOfBoundsException e){
            /* If no file was passed on the command line, this expception is
			generated. A message indicating how to the class should be
			called is displayed */
			System.out.println("Usage: java ReadFile filename\n");			

		}catch (IOException e){
			// If another exception is generated, print a stack trace
            e.printStackTrace();
        }
        
    }// end main
}
