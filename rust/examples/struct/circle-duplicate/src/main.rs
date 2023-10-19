struct Point {
    x: i32,
    y: i32,
}

struct Circle {
    x: i32,
    y: i32,
    radius: i32,
}

impl Point {
    fn mv(&mut self, dx: i32, dy: i32) {
        self.x += dx;
        self.y += dy;
    }
}

impl Circle {
    fn mv(&mut self, dx: i32, dy: i32) {
        self.x += dx;
        self.y += dy;
    }
    fn area(&self) -> f32 {
        (self.radius as f32) * (self.radius as f32) * (std::f64::consts::PI as f32)
    }
}


fn main() {
    let mut p = Point {x: 2, y: 3};
    println!("{}", p.x);
    println!("{}", p.y);
    println!();

    p.mv(4, 5);
    println!("{}", p.x);
    println!("{}", p.y);
    println!("----");

    let mut a = Circle {x: 2, y: 3, radius: 7};
    println!("{}", a.x);
    println!("{}", a.y);
    println!("{}", a.radius);
    println!("{}", a.area());
    println!();

    a.mv(4, 5);
    println!("{}", a.x);
    println!("{}", a.y);
    println!("{}", a.radius);
}
