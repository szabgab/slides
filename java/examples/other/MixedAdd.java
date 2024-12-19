public class MixedAdd {
    public static void main(String[] args) {
        String a = "19";
        String b = "23";
        int c = 23;
        double d = 2.3;
        float f = 2.3f;
        System.out.println("The sum: " + (a+b));
        System.out.println("The sum: " + (a+c));
        System.out.println("The sum: " + (a+d));
        System.out.println("The sum: " + (a+f));
        System.out.println("The sum: " + (f+a));


        // MixedAdd.java:16: error: bad operand types for binary operator '*'
        // String line = "-";
        // System.out.println(line * 23);
    }
}
