class Point {
  double x;
  double y;
  
  Point(this.x, this.y);
}

class Circle extends Point {
  double r;
  
  Circle(double x, double y, this.r) : super(x, y);

/*
  toString() {
    return "($x, $y, $r)";
  }
*/

}


main() {
   Point p = new Point(2.0, 3.0);
   print(p);    // Instance of 'Point'
   print(p.x);  // 2.0
   print(p.y);  // 3.0
   
   var c = new Circle(4.0, 5.0, 2.5);
   print(c);    // Instance of 'Circle'     (4.0, 5.0, 2.5)
   print(c.x);  // 4.0
   print(c.y);  // 5.0
   print(c.r);  // 2.5
}
