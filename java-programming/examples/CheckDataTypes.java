public class CheckDataTypes {
    public static void main(String[] args) {
        // https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html
        System.out.println("Checking Data Types");
        String h = "Hello";
        String w = "World";
        System.out.println(h);     // Hello
        System.out.println(w);     // World
        String full = h + " " + w;
        System.out.println(full);  // Hello World


        // int is 32 bit sigend between -2^31 and 2^31-1
        int val1 = 19;
        int val2 = 23;
        int val3 = val1 + val2;
        System.out.println(val3);  // 42

        // double 64-bit IEEE 754 floating point.
        double db1 = 19.3;
        double db2 = 22.7;
        double db3 = db1 + db2;
        System.out.println(db3);  // 42.0

        boolean b = true;
        System.out.println(b);  // true
        b = ! b;
        System.out.println(b);  // false


        if (!b) {
            System.out.println("yeah");
            System.out.println("works");
        }
        // Actually if there is only a single statement in the block you don't even need the curly braces, but I would recommend this practice:
        if (!b)
            System.out.println("this too");

        // because of this:
        if (b)
            System.out.println("in condition");
            System.out.println("NOT in condition"); // this is not inside the condition even though the indentation seems to suggest that.

    }
}
