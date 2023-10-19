struct Point {
    x: i32,
    y: i32,
}

struct Circle {
    point: Point,
    radius: i32,
}

impl Point {
    fn mv(&mut self, dx: i32, dy: i32) {
        self.x += dx;
        self.y += dy;
    }
}

impl Circle {
    fn area(&self) -> f32 {
        (self.radius as f32) * (self.radius as f32) * (std::f64::consts::PI as f32)
    }
}


fn main() {
    let mut a = Circle {point: Point {x: 2, y: 3}, radius: 7};
    println!("{}", a.point.x);
    println!("{}", a.point.y);
    println!("{}", a.radius);
    println!("{}", a.area());
    println!();

    a.point.mv(4, 5);
    println!("{}", a.point.x);
    println!("{}", a.point.y);
    println!("{}", a.radius);
}
