fn main() {
    let text = String::from("Black cat, brown cat, many cats and a dog");
    println!("{text}");

let new = text.replace("cat", "mouse");
    println!("{new}");
    println!("{text}");
}
