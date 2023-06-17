fn main() {
    add(3, 4);
    add("x", "y");
}

fn add(x: i32, y: i32) {
    let z = x+y;
    println!("{z}");
}

fn add(x: &str, y: &str) {
    println!("{x}{y}");
}
