struct Point {
    x: i32,
    y: i32
}

impl Point {
    fn mv(&mut self, dx: i32, dy: i32) {
        self.x += dx;
        self.y += dy;
    }
}

fn main() {
    let mut a = Point {x: 2, y: 3};
    println!("{}", a.x);
    println!("{}", a.y);

    a.mv(4, 5);
    println!("{}", a.x);
    println!("{}", a.y);
}
