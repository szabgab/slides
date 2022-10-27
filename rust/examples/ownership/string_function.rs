fn main() {
    let name = String::from("Foo Bar");
    greet(name);
    // greet(name);  // use of moved value: `name`
}

fn greet(text: String) {
    println!("Greet: {text}");
}


