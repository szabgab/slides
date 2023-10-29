fn main() {
    let name = "Foo Bar";
    greet(name);
    greet(name);
}

fn greet(text: &str) {
    println!("Greet: {text}");
}
