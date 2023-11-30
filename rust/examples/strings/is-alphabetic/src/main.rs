fn main() {
    let strings = vec!["text", "t xt", "t,xt", "😇😈", "Ωأㅏñ", "שלום"];

    for text in &strings {
        println!("{}: {}", text, text.chars().all(|chr| chr.is_alphabetic()));
    }
    println!();

    for text in &strings {
        println!("{}: {}", text, text.chars().all(char::is_alphabetic));
    }
    println!();

    for text in strings {
        println!(
            "{}: {}",
            text,
            text.chars().all(|chr| chr.is_alphabetic() || chr == ' ')
        );
    }
}
