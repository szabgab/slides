public class Convert {
    public static void main(String[] args) {
        String number_str = "23";
        int a_number      = 19;
        System.out.println(number_str);              // 23
        System.out.println(number_str + a_number);   // 2319

        int real_number = Integer.parseInt(number_str);
        System.out.println(real_number + a_number);  // 42
    }
}
