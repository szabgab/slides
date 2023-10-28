#[allow(clippy::assign_op_pattern)]
fn main() {
    let mut x: i8 = 126;
    println!("{x}");

    x = x + 1;
    println!("{x}");

    x += 1;
    println!("{x}");
}
