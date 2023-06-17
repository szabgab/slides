fn main() {
    let mut name = "Foo";
    let other = name;
    println!("{name}");
    println!("{other}");
    name = "Foo Bar";
    // name.push_str(" Bar");
    // no method named `push_str` found for reference `&str`
    println!("{name}");
    println!("{other}");
}
