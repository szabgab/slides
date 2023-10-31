fn main() {
    let things = (11, '2', String::from("three"), 19, 23);

    let (a, b, c, _, e) = &things; // deconstructing the tuple
    println!("{a}");
    println!("{b}");
    println!("{c}");
    println!("{e}");
    println!();

    let (x, y) = (&things.2, &things.4);
    println!("{x}");
    println!("{y}");
}
