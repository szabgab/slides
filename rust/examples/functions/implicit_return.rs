fn main() {
    let x = 2;
    println!("{x}");

    let y = add(2, 3);
        println!("{y}");
}

fn add(a: i32, b: i32) -> i32 {
    a + b   // no semi-colon here!
}
