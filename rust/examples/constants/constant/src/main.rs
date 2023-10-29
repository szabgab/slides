#[allow(clippy::approx_constant)]
fn main() {
    const NAME: &str = "Foo";
    println!("{}", NAME);

    const PI: f64 = 3.14;
    println!("{}", PI);
    // PI = 3.1; // cannot assign to this expression

    const DAY: i32 = 60 * 60 * 24;
    println!("{}", DAY);
}
