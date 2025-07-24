class MethodOverloading {
    public static void main(String[] args) {
        System.out.println("main");
        MethodOverloading.hello();
        MethodOverloading.hello("Brave New World");
        MethodOverloading.hello(42);
    }
    public static void hello() {
       System.out.println("hello");
    }
    public static void hello(String message) {
       System.out.println("hello with message: " + message);
    }
    public static void hello(int answer) {
        System.out.println("the answer is: " + answer);
     }
}

