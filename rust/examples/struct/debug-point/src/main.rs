use std::fmt;

struct Point {
    x: i32,
    y: i32,
}

impl std::fmt::Debug for Point {
    fn fmt(&self, format: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(format, "Point(x: {}, y: {})", self.x, self.y)
    }
}

fn main() {
    let pnt = Point { x: 2, y: 3 };

    dbg!(pnt);
}
