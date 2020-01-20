class Point {
  double x;
  double y;
  
  move(dx, dy) {
    x += dx;
    y += dy;
  }
  
  Point(sx, sy) {
    x = sx;
    y = sy;
  }
}

main() {
   Point p = new Point(2.0, 3.0);
   print(p);    // Instance of 'Point'
   print(p.x);  // 2.0
   p.x = 4.0;
   print(p.x);  // 4.0
}