fn main() {
    println!("{}", add(2, 3));
    println!("{}", add(3, 4));
}

fn add(a: i32, b: i32) -> i32 {
    a + b   // no semi-colon here!
}
