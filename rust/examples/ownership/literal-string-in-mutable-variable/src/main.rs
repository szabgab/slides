fn main() {
    let mut name = "Foo";
    let other = name;
    println!("{name}");
    println!("{other}");

    name = "Foo Bar";

    //name.push_str(" Bar");

    println!("{name}");
    println!("{other}");
}
