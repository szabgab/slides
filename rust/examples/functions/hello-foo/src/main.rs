fn main() {
    greet("Foo");
    greet("Bar");
    println!();

    let name = "Foo";
    greet(name);
    greet(name);
    println!();

    let name = "Bar".to_string();
    greet(&name);
    greet(&name);
}

fn greet(name: &str) {
    println!("Hello {}!", name);
}
