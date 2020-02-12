public class Bike {
    private static int count = 0;
    public static int getCount() {
        return Bike.count;
    }
    public Bike() {
        Bike.count++;
    }
    public void finalize() {
        Bike.count--;
        System.out.println("Finalize");
    }
}
