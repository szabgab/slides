fn main() {
    let text = " 2.3 ";
    println!("'{}'", text);
    let number: f32 = text
        .trim()
        .parse()
        .expect("Could not convert to f32");

    println!("'{}'", number);
    println!("'{}'", number + 1.0);
}
