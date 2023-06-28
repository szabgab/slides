fn main() {
    let str1 = "Hello";
    let str2 = "World";

    // let text = str1 + str2; // cannot add `&str` to `&str`
    let text = str1.to_string() + " " + str2;
    println!("{}", text);
}

