public class Point {
    private int x;
    private int y;

    public Point(int a, int b) {
        x = a;
        y = b;
    }

    public String showCoord() {
        return "(" + x + ", " + y + ")";
    }

    public void move(int dx, int dy) {
        x += dx;
        y += dy;
    }

    public int getx() {
        return x;
    }
    public int gety() {
        return y;
    }
}
