fn main() {
    let string1 = String::from("Apple");
    let string2 = String::from("Banana");

    let text = string1.clone() + &string2;  // we move strin1 and then copy the content of string2
    println!("{}", text);
    println!("{}", string2);
    println!("{}", string1);
}

