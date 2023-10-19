struct Point {
    x: i32,
    y: i32
}

fn main() {
    let mut a = Point {x: 2, y: 3};
    println!("{}", a.x);
    println!("{}", a.y);

    a.y = 7;
    println!("{}", a.y);
}
