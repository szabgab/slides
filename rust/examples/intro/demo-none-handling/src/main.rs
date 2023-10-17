fn say_hi(name: Option<String>) {
    match name {
        Some(text) => println!("Hello {text}"),
        None => println!("Welcome! My name is Rust."),
    }
}



fn main() {
    let name = get_name(true);
    say_hi(name);

    let name = get_name(false);
    say_hi(name);
}

fn get_name(good: bool) -> Option<String> {
    if good {
        Some("Gabor".to_string())
    } else {
        None
    }
}


