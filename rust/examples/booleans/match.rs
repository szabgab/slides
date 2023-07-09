fn greet(text: &str) {
    match text {
        "morning" => println!("Good morning"),
        "night" => println!("Goodnight"),
        // "morning" => println!("Again"),  warning: unreachable pattern
        "Jane" | "Joe" => println!("Hello {text}"),
        _ => println!("Hello World!"),
    }
}

fn main() {
    greet("morning");
    greet("night");
    greet("Jane");
    greet("Joe");
    greet("George");
}


