fn main() {
    let things = (11, '2', String::from("three"));
    println!("{}", things.0);
    println!("{}", things.1);
    println!("{}", things.2);
    println!("{:?}", things);

    // Optionally we can define the types
    let other: (i32, char, String) = (11, '2', String::from("three"));
    println!("{:?}", other);

    let (a, b , c) = other; // deconstructing the tuple
    println!("{a}");
    println!("{b}");
    println!("{c}");
}
