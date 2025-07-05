public class AddCmdLineNumbers{
    public static void main(String[] args){
        if (args.length != 2) {
            System.out.println("Must have exactly 2 values on the command line");
            System.exit(1);
        }
        System.out.println("First: " + args[0]);
        System.out.println("Second: " + args[1]);
        System.out.println(Integer.parseInt(args[0]) + Integer.parseInt(args[1]));
    }
}


