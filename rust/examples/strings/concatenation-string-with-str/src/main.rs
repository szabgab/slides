fn main() {
    let str1 = "Hello";
    let string1 = String::from("Apple");

    //let text = str1 + string1; // cannot add `String` to `&str`
    let text = string1 + str1;
    println!("{}", text);
}

