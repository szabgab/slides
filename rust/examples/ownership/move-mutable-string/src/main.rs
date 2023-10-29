fn main() {
    let name = String::from("Foo");
    println!("{name}");

    let other = name;
    println!("{other}");

    // println!("{name}"); // value borrowed here after move
}
