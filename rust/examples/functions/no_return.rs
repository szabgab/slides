fn main() {
    println!("Before");
    greet();
    greet_me("Foo Bar");
    println!("After");
}

fn greet() {
    println!("Hello World!");
}

fn greet_me(name: &str) {
    println!("Hello {name}!");
}
