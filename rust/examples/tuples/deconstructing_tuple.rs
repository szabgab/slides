fn main() {
    let things = (11, '2', String::from("three"));

    let (a, b , c) = things; // deconstructing the tuple
    println!("{a}");
    println!("{b}");
    println!("{c}");
}
