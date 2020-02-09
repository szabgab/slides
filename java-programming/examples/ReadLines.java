import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;

public class ReadLines {
    public static void main(String[] args) throws IOException {
        if (args.length != 1) {
            System.out.println("Must have exactly 1 value on the command line");
            System.exit(1);
        }
        String filename = args[0];


        BufferedReader inputStream = null;

        try {
            inputStream = new BufferedReader(new FileReader(filename));

            String line;
            while ((line = inputStream.readLine()) != null) {
                System.out.println(line);
            }
        } finally {
            if (inputStream != null) {
                inputStream.close();
            }
        }
    }
}
