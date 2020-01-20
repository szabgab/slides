public class AddCmdLineArgs{
    public static void main(String[] args){
        if (args.length != 2) {
            System.out.println("Must have exactly 2 values on the command line");
            System.exit(1);
        }
        System.out.println("Input: " + args[0]);
        System.out.println("Input: " + args[1]);
        System.out.println(args[0] + args[1]);
    }
}

