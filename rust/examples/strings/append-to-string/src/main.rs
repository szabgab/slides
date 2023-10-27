fn main() {
    let mut text = String::from("");
    println!("{text}");

    text.push('a');
    println!("{text}");

    text.push_str("bcd");
    println!("{text}");

    let literal_string = "x";
    text.push_str(literal_string);
    println!("{text}");

    let string = String::from("yz");
    text.push_str(&string);
    println!("{text}");

    let cr = 'e';
    text.push_str(&cr.to_string());
    println!("{text}");
}
