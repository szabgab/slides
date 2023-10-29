fn main() {
    let name = String::from("Foo Bar");
    println!("{name}");
    greet(&name);
    println!("{name}"); // borrow of moved value: `name`
    // greet(name);     // use of moved value: `name`
}

fn greet(text: &str) {
    println!("Greet: {text}");
}


