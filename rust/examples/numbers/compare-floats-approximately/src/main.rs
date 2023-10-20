use float_cmp::approx_eq;

fn main() {
    let x = 1.0;
    let y = 2.0;
    let z = 1.0;
    println!("{}", x < y);
    println!("{}", x == z);
    println!();


    let x = 0.1 + 0.2;
    let y = 0.3;
    println!("{}", x);
    println!("{}", y);
    println!("{}", x == y);
    println!("{}", approx_eq!(f32, x, y, ulps = 17));

    let x = 0.00001;
    let y = 0.000010000001;
    println!("{}", x == y);
    println!("{}", approx_eq!(f32, x, y, ulps = 20));
}
