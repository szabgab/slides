fn main() {
    let x = 1;
    let y = 2;

    let z = if x < y {
        x + y
    } else {
        x * y
    };

    println!("{z}");
}
