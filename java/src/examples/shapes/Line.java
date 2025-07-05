import java.lang.Math;

public class Line {
    private Point a;
    private Point b;

    public Line(Point aa, Point bb) {
        a = aa;
        b = bb;
    }

    public String showLine() {
        return a.showCoord() + "___" + b.showCoord();
    }

    public double length() {
        return Math.pow(Math.pow(a.getx()-b.getx(), 2) + Math.pow(a.gety()-b.gety(), 2), 0.5);
    }
}
