fn main() {
    let text = "23";
    println!("'{}'", text);
    println!();

    let number: i32 = text
        .parse()
        .expect("Could not convert to i32");

    println!("'{}'", number);
    println!("'{}'", number + 1);
    println!();

    let number = text
        .parse::<i32>()
        .expect("Could not convert to i32");
    println!("'{}'", number);
    println!("'{}'", number + 1);
}
