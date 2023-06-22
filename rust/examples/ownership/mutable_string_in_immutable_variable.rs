fn main() {
    let name = String::from("Foo");
    println!("{name}");

    name.push_str(" Bar");

    let name = String::from("Bar");
    println!("{name}");
}
