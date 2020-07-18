public class RunCode {
    public static void main(String[] args) {
        System.out.println("Hello");
        Point p1 = new Point(2, 3);
        System.out.println(p1);
        // System.out.println(p1.x);  //  x has private access in Point
        System.out.println(p1.showCoord());
        p1.move(3, 7);
        System.out.println(p1.showCoord());

        Point p2 = new Point(2, 6);
        System.out.println(p2.showCoord());

        Line line = new Line(p1, p2);
        System.out.println(line.showLine());
        System.out.println(line.length());
    }
}
