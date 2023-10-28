fn main() {
    let mut a = 23;
    println!("{a}");

    let mut b = a;
    println!("{b}");

    a += 1;
    println!("{a}");
    println!("{b}");

    b += 1;
    println!("{a}");
    println!("{b}");
}
