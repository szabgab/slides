public class TryClass {
    public static void main(String[] args) {
        System.out.println("Hello");
        Person p1 = new Person("Joe");
        System.out.println(p1);        // Person@2a139a55
        System.out.println(p1.name);   // Joe

        Person p2 = new Person("Jane");
        System.out.println(p2);        // Person@15db9742
        System.out.println(p2.name);   // Jane

        p1.name = "Joseph";
        System.out.println(p1.name);   // Joseph
        System.out.println(p2.name);   // Jane

        // System.out.println(p2.id);   // will not compile

        Worker w1 = new Worker("Zorg", 23);
        System.out.println(w1.name);   // Zorg
        System.out.println(w1.id);     // 23
    }
}
