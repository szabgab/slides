fn main() {
    let string1 = String::from("Apple");
    let string2 = String::from("Banana");

    //let text = string1 + string2; // mismatched types
    let text = string1 + &string2;
    println!("{}", text);
}


