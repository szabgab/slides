public class TryPoint {
    public static void main(String[] args) {
        Point a = new Point(2, 3);
        System.out.println(a);
        System.out.println(a.x);
        a.x = 7;
        System.out.println(a.x);
        //System.out.println(a.getX);
    }
}
