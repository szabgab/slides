fn main() {
    let x:f64 = 0.1 + 0.2;
    let y = 0.3;
    println!("{}", x);
    println!("{}", y);
    println!("{}", x == y);
    println!();

    println!("{}", (100.0 * x).round() / 100.0);
    println!("{}", ((100.0 * x).round() / 100.0) == y);
    println!("{}", round64(x, 100.0));
    println!("{}", round64(x, 100.0) == y);
}

fn round64(number:f64, precision:f64) -> f64{
    (precision * number).round() / precision
}
