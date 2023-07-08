struct Point {
    x: i32,
    y: i32
}

fn main() {
    let a = Point {x: 2, y: 3};
    println!("{}", a.x);
    println!("{}", a.y);

    // a.y = 7; // cannot assign to `a.y`, as `a` is not declared as mutable
    // println!("{}", a.y);
}
