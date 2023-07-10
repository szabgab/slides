fn main() {
    let pi = 3.1415926535897932384626433;
    println!("{pi}");
    println!("{:.2}", pi);
    let rpi = (pi * 100.0 as f64).round() / 100.0;
    println!("{rpi}");

    let xpi = (pi * 10000.0 as f64).round() / 10000.0;
    println!("{xpi}");

    println!("");

    let x:f32 = 3.14159;
    println!("{x}");
    println!("{:.2}", x);
    let y = (x * 100.0).round() / 100.0;
    println!("{y}");
}
