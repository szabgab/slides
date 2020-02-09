//import java.io.BufferedReader;
import java.io.InputStream;
import java.io.IOException;

class Runls {
    public static void main(String[] args) {
        try
        {
            // Command to create an external process
            String command = "ls";
            InputStream iStream = null;

            // Running the above command
            Runtime run  = Runtime.getRuntime();
            Process proc = run.exec(command);
            iStream = proc.getInputStream();
            int line;
            while ((line = iStream.read()) != -1) {
                System.out.println(line);
            }

        }
        catch (IOException e) {
            e.printStackTrace();
        }
   }
}
