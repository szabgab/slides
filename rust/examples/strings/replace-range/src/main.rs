fn main() {
    let mut text = String::from("The black cat climbed the green tree");
    println!("{text}");

    text.replace_range(10..13, "dog");
    println!("{text}");

    text.replace_range(10..13, "elephant");
    println!("{text}");
}
