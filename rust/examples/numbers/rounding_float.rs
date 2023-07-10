fn main() {
    let pi = 3.1415926535897932384626433;
    println!("{pi}");
    println!("{:.2}", pi);
    let rpi = (pi * 100.0 as f64).round() / 100.0;
    println!("{rpi}");
}
