fn main() {
    let text = "23\n";
    println!("'{}'", text);
    let number: i32 = text
        .trim()
        .parse()
        .expect("Could not convert to i32");

    println!("'{}'", number);
    println!("'{}'", number + 1);
}
