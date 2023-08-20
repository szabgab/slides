fn main() {
    let text = "The Green cat";
    println!("{}", text);
    println!("{}", text.to_lowercase());             // on &str
    println!("{}", text.to_string().to_lowercase()); // on String

    println!("{}", text.to_uppercase());             // on &str
}
