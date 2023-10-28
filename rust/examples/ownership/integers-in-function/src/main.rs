fn add_integers(x: i32, y: i32) -> i32 {
    let z = x + y;
    #[allow(clippy::needless_return)]
    return z;
}

fn main() {
    let a = 23;
    println!("{a}");

    let b = 19;
    println!("{b}");
    println!();

    let c = add_integers(a, b);
    println!("{a}");
    println!("{b}");
    println!("{c}");
}
