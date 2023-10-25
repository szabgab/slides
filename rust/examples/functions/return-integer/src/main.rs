fn main() {
    println!("{}", add(2, 3));
    println!("{}", add(3, 4));
}

fn add(x: i32, y: i32) -> i32 {
    #[allow(clippy::needless_return)]
    return x + y;
}
