#[allow(clippy::assign_op_pattern)]
fn main() {
    let mut x = 1;
    println!("{x}");

    x = x + 1;
    println!("{x}");

    x += 1;
    println!("{x}");

    // Rust has no prefix and postfix increment operator
    // x++;
    // ++x;
}
