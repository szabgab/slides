fn main() {
    greet("Foo");
    greet("Bar");
}

fn greet(name: &str) {
    println!("Hello {}!", name);
}
