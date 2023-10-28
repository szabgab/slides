fn main() {
    let text = String::from("Black cat, brown cat, many cats and a dog");
    println!("{text}");

    let new = text.replacen("cat", "mouse", 2);
    println!("{new}");
    println!("{text}");
}

