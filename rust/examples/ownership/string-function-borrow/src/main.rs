fn main() {
    let name = String::from("Foo Bar");
    greet(&name);
    greet(&name);
}

fn greet(text: &String) {
    println!("Greet: {}", *text); // explicit derefernce
    println!("Greet: {}", text);  // automatic dereference
    println!("Greet: {text}");
}

