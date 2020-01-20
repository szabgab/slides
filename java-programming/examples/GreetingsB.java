class Greeting {
    public static void hello() {
       System.out.println("Hello World");
    }
    public static void hello(String message) {
       System.out.println("Hello World " + message);
    }
}

public class Greetings {
    public static void main(String[] args) {
        System.out.println("Hello");
        Greeting.hello();
        Greeting.hello("Brave New World");
    }
}


