fn main() {
    let text = "The black cat climbed the green tree!";
    println!("{}", text);
    println!("'{}'", &text[4..4]);
    println!("'{}'", &text[4..=4]);
    println!("'{}'", &text[4..5]);
    println!("'{}'", &text[4..9]);
    println!("'{}'", &text[4..=8]);
    println!("'{}'", &text[4..]);
    println!("'{}'", &text[4..text.len()]);
    println!("'{}'", &text[4..text.len()-1]);
    println!("'{}'", &text[..4]);

    println!("'{}'", &text[4..40]);  // thread 'main' panicked at 'byte index 40 is out of bounds
}
