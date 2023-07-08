fn stats(a: f32, b: f32) -> (f32, f32) {
    (a + b, a * b)
}
fn main() {
    let (sum, multiple) = stats(4.0, 7.0);
    println!("{sum}, {multiple}");
}
