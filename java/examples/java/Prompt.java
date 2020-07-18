import java.io.*;

class Prompt{
    public static void main(String[] args) throws IOException{
        System.out.print("Your name: ");
        InputStreamReader converter = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(converter);
        String name = in.readLine();
        System.out.println("Your name is: " + name);
    }
}

